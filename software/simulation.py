import datetime
from rocketpy import Environment, Rocket, SolidMotor, Flight
import math
from matplotlib import pyplot as plt


body_length = 1.70
body_radius = 0.05

ground_level = 165
env = Environment(
    latitude=39.3897,
    longitude=-8.28896388889,
    elevation=ground_level,
    date=(2023, 10, 15, 12)
)

signy = Rocket(
    radius=0.05,
    mass= 7.920, # Rocket (no casing)
    inertia=(4.6, 4.6, 0.015), # from open rocket
    power_off_drag=0.58, # from open rocket
    power_on_drag=0.59, # from open rocket
    center_of_mass_without_motor=1.20,
    coordinate_system_orientation="nose_to_tail"
)

pro75l2375 = SolidMotor(
    thrust_source="Cesaroni_4864L2375-P.eng",
    dry_mass = 1.840,
    center_of_dry_mass = 0.65 / 2, #TODO (the total CG differs by 3cm to open rocket so this is pretty good)
    dry_inertia = (0, 0, 0), #TODO
    grains_center_of_mass_position = 0.65 / 2,
    grain_number = 4,
    grain_density = 1815, # from docs
    grain_outer_radius = 0.033,
    grain_initial_inner_radius = 0.015,
    grain_initial_height = 0.12,
    grain_separation = 0.005,
    nozzle_radius = 0.033,
    interpolation_method="linear",
    coordinate_system_orientation="nozzle_to_combustion_chamber"
)

signy.add_motor(pro75l2375, 2.475)

signy.add_nose(
    length=0.40,
    kind="Von Karman",
    position=0,
)

fins = signy.add_trapezoidal_fins(
    4,
    root_chord=0.18,
    tip_chord=0.18,
    span=0.08,
    position=2.275,
    sweep_angle=45
)

# fins.draw()

signy.set_rail_buttons(155, 245)

reefed_cd = 0.9
reefed_radius = 0.4
signy.add_parachute('Reefed',
                    cd_s=reefed_cd * reefed_radius ** 2 * math.pi,
                    trigger="apogee")


main_cd = 1.3
main_radius = 0.98
signy.add_parachute('Main',
                    cd_s=main_cd * main_radius ** 2 * math.pi,
                    trigger=300)


test_flight = Flight(rocket=signy, environment=env, rail_length=12, inclination=86, heading=0)

signy.all_info()
test_flight.all_info()
# test_flight.animate()
# test_flight.plot_3d_trajectory()
# test_flight.z.plot()
# test_flight.vz.plot()
# test_flight.az.plot()
# print(test_flight.parachute_events)