import datetime
from rocketpy import Environment, Rocket, HybridMotor, Flight
import math
from matplotlib import pyplot as plt


body_length = 1.70
body_radius = 0.05


env = Environment(
    railLength=12,
    latitude=39.3897,
    longitude=-8.28896388889,
    elevation=165,
    date=(2023, 8, 20, 14)
)

# env.setAtmosphericModel(type='Forecast', file='GFS')

motor = HybridMotor(
    thrustSource = 1300.0, # N
    burnOut = 4, # s
    grainNumber = 1,
    grainDensity = 900, # kg/m3
    grainOuterRadius = 0.0345, # m
    grainInitialInnerRadius = 0.015, # m
    grainInitialHeight = 0.270, # m
    oxidizerTankRadius = 0.045, # m
    oxidizerTankHeight = 0.860, # m
    oxidizerInitialPressure = 40, # atmospheres?
    oxidizerDensity = 1200.0, # kg/m3
    oxidizerMolarMass = 44.01, # g/mol
    oxidizerInitialVolume = math.pi * 0.045 ** 2 * 0.860,
    distanceGrainToTank = 0.270 / 2,
    injectorArea = 0.003 ** 2 * math.pi * 2,
    # grainSeparation=0,
    # nozzleRadius=0.0335,
    # throatRadius=0.0114,
    # reshapeThrustCurve=False,
    # interpolationMethod="linear",
)

signy = Rocket(
    motor=motor,
    radius=0.05,
    mass=9,
    inertiaI=6.60,
    inertiaZ=0.0351,
    distanceRocketNozzle=-1,
    distanceRocketPropellant=-0.7,
    powerOffDrag= 0.75,
    powerOnDrag= 0.75,
)

signy.addNose(
    length=0.6,
    kind="conical",
    distanceToCM=0.9
)

fin = signy.addTrapezoidalFins(
    4,
    span=0.087,
    rootChord=0.18,
    tipChord=0.09,
    distanceToCM=-1.2
)

# fin.draw()

signy.setRailButtons([0.3, -0.4])

signy.addTail(
    topRadius=0.0635,
    bottomRadius=0.0435,
    length=0.060,
    distanceToCM=-1.194656
)

def drogueTrigger(p, y):
    return True if y[5] < 0 else False

def mainTrigger(p, y):
    ret = True if y[5] < 0 and y[2] < 700 else False
    return ret



signy.addParachute('Drogue',
                              CdS=0.8 * 0.41 ** 2 * math.pi,
                              trigger=drogueTrigger,
                              samplingRate=105,
                              lag=1.5,
                              noise=(0, 8.3, 0.5))

signy.addParachute('Main',
                            CdS=1.5 * 1 ** 2 * math.pi,
                            trigger=mainTrigger,
                            samplingRate=105,
                            lag=1.5,
                            noise=(0, 8.3, 0.5))


test_flight = Flight(rocket=signy, environment=env, inclination=84, heading=90)

signy.allInfo()
test_flight.allInfo()
test_flight.animate()
test_flight.plot3dTrajectory()
test_flight.z.plot()
test_flight.vz.plot()
test_flight.az.plot()
print(test_flight.parachuteEvents)