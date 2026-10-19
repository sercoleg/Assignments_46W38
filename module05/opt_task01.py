import numpy as np
import time

from main import wind_turbine_power_output

def wind_turbine_power_output_vectorized(
        wind_speed,
        rated_power=15,
        cut_in_wind_speed=3,
        rated_wind_speed=11,
        cut_out_wind_speed=25,
        interpolation_method='linear'):
    """
    Calculates the power output in MW of a public 15 MW wind turbine.

    Parameters
    ----------
    wind_speed : array_like
        Wind speed [m/s]. It can be a scalar or a NumPy array
        with any shape.

    rated_power : float, default=15
        Rated power [MW].

    cut_in_wind_speed : float, default=3
        Cut-in wind speed [m/s].

    rated_wind_speed : float, default=11
        Rated wind speed [m/s].

    cut_out_wind_speed : float, default=25
        Cut-out wind speed [m/s].

    interpolation_method : str, default='linear'
        Interpolation method: 'linear' or 'cubic'.

    Returns
    -------
    power_output : numpy.ndarray or numpy scalar
        Power output [MW] with the same shape as wind_speed.
    """

    # Convert the input into a NumPy array
    wind_speed = np.asarray(wind_speed)

    # Define weighting function g
    if interpolation_method == 'linear':
        g = ((wind_speed - cut_in_wind_speed) / (rated_wind_speed - cut_in_wind_speed))

    elif interpolation_method == 'cubic':
        g = wind_speed**3 / rated_wind_speed**3

    else:
        raise ValueError("interpolation_method should be 'linear' or 'cubic'")

    # Start with zero power for all wind speeds
    power_output = np.zeros_like(wind_speed, dtype=float)

    # Mask for the partial-load region
    partial_load_mask = ((wind_speed >= cut_in_wind_speed)
                         & (wind_speed < rated_wind_speed))

    # Mask for the rated-power region
    rated_power_mask = ((wind_speed >= rated_wind_speed)
                        & (wind_speed < cut_out_wind_speed))

    # Assign power output according to each operating region
    power_output[partial_load_mask] = (g[partial_load_mask] * rated_power)
    power_output[rated_power_mask] = rated_power

    return power_output

if __name__ == '__main__':

    wind_speeds = np.linspace(0, 30, 1_000_000)
    start_time = time.time()

    power_scalar = []

    for v in wind_speeds:
        power_scalar.append(wind_turbine_power_output(v))

    scalar_time = time.time() - start_time

    start_time = time.time()

    power_vectorized = wind_turbine_power_output_vectorized(wind_speeds)

    vectorized_time = time.time() - start_time

    print(f"Scalar time: {scalar_time:.6f} seconds")
    print(f"Vectorized time: {vectorized_time:.6f} seconds")

    power_scalar = np.array(power_scalar)
    print(np.allclose(power_scalar, power_vectorized))

    speedup = scalar_time / vectorized_time

    print(f"Speedup: {speedup:.1f} times")
