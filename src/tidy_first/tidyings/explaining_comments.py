"""Part 1, Chapter 14 - Explaining Comments"""

# example adapted from https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.atmosphere.gueymard94_pw.html#pvlib.atmosphere.gueymard94_pw

import math

import hypothesis
import hypothesis.strategies as st

Input = tuple[float, float]
Output = float


@hypothesis.given(
    st.tuples(
        st.floats(min_value=-273, max_value=1000),
        st.floats(min_value=0, max_value=100),
    )
)
def run(args: Input) -> None:
    assert before(*args) == after(*args)


# fmt: off

def before(air_temp_in_c: float, relative_humidity: float) -> Output:
    """Calculates precipitable water from air temp & relative humidity"""
    T = air_temp_in_c + 273.15
    theta = T / 273.15
    pw = (
        0.1 *
        (0.4976 + 1.5265*theta + math.exp(13.6897*theta - 14.9188*(theta)**3)) *
        (216.7*relative_humidity/(100*T)*math.exp(22.330 - 49.140*(100/T) - 10.922*(100/T)**2 - 0.39015*T/100))
    )
    return max([pw, 0.1])


def after(air_temp_in_c: float, relative_humidity: float) -> Output:
    """Calculates precipitable water from air temp & relative humidity.

    The accuracy of this method is approximately 20% for moderate PW (1-3cm)
    and less accurate otherwise.

    ## References
    .. [1] W. M. Keogh and A. W. Blakers, Accurate Measurement, Using Natural
       Sunlight, of Silicon Solar Cells, Prog. in Photovoltaics: Res.
       and Appl. 2004, vol 12, pp. 1-19 (:doi:`10.1002/pip.517`)

    .. [2] C. Gueymard, Analysis of Monthly Average Atmospheric Precipitable
       Water and Turbidity in Canada and Northern United States,
       Solar Energy vol 53(1), pp. 57-71, 1994.

    .. [3] C. Gueymard, Assessment of the Accuracy and Computing Speed of
       simplified saturation vapor equations using a new reference
       dataset, J. of Applied Meteorology 1993, vol. 32(7), pp.
       1294-1300.
    """
    T = air_temp_in_c + 273.15  # convert celius to kelvin
    theta = T / 273.15
    # Eq. 1 from Keogh and Blakers (Pw = 0.1 H_v \rho_v)
    pw = (
        0.1 *
        # H_v
        (0.4976 + 1.5265*theta + math.exp(13.6897*theta - 14.9188*(theta)**3)) *
        # rho_v (rho_v = 216.7 R_H e_s / T)
        (
            216.7 *
            relative_humidity / (100*T) *
            # e_s
            math.exp(22.330 - 49.140*(100/T) - 10.922*(100/T)**2 - 0.39015*T/100)
        )
    )
    return max([pw, 0.1])

# fmt: on

if __name__ == "__main__":
    run()
