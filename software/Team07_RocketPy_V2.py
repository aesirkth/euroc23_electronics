import datetime
from rocketpy import Environment, Rocket, SolidMotor, Flight
import math
from matplotlib import pyplot as plt


ground_level = 165
env = Environment(
    latitude=39.3897,
    longitude=-8.28896388889,
    elevation=ground_level,
    date=(2023, 10, 15, 12),
)

env.set_atmospheric_model("custom_atmosphere", wind_u=-5, wind_v=-5)

signy = Rocket(
    radius=0.05,
    mass= 8.298, # Rocket (no casing)
    inertia=(4.6, 4.6, 0.015), # from open rocket
    power_off_drag=0.58, # from open rocket
    power_on_drag=0.59, # from open rocket
    center_of_mass_without_motor=1.20,
    coordinate_system_orientation="nose_to_tail"
)

pro75l2375 = SolidMotor(
    thrust_source="Cesaroni_4864L2375-P.eng",
    dry_mass = 1.840,
    center_of_dry_mass = 0.325,
    dry_inertia = (0.004591,  0.004591, 0.009183),
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

signy.add_motor(pro75l2375, 2.45)

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
    position=2.29,
    sweep_angle=135
)

signy.set_rail_buttons(1.55, 2.45)

spill_radius = 0.4 / 2

reefed_cd = 0.8
reefed_radius = 0.7 / 2
signy.add_parachute('Reefed',
                    cd_s=reefed_cd * math.pi * (reefed_radius ** 2 - spill_radius ** 2),
                    trigger="apogee", lag=3)


main_cd = 1.0
main_radius = 2.13 / 2
signy.add_parachute('Main',
                    cd_s=main_cd * math.pi * (main_radius ** 2 - spill_radius ** 2),
                    trigger=200)



# signy.all_info()

# signy.evaluate_static_margin()
# signy.evaluate_center_of_mass()
# print("margin", signy.static_margin.get_value(0), signy.static_margin.get_value(4))
# print("CoG", signy.center_of_mass.get_value(0), signy.center_of_mass.get_value(4))
# print("CoP", signy.cp_position)


test_flight = Flight(rocket=signy, environment=env, rail_length=12, inclination=84, heading=0)
# fins.draw()
# test_flight.animate()
test_flight.all_info()
# test_flight.animate()
# test_flight.z.plot()
# test_flight.vz.plot()
# test_flight.az.plot()
# print(test_flight.parachute_events)