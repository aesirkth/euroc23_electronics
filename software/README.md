## Simulations for team 07 euroc23

[Repository](https://github.com/aesirkth/euroc23_electronics/tree/master/software)

### installation
There is a recent version of RocketPy bundled with the repo. You will still need all dependencies for RocketPy v1.0.0 prerelease so either install that with `pip install rocketpy --pre` and `pip install rocketpy[env_analysis]` or the requirements.txt with `pip install -r requirements.txt`.

Using the system's RocketPy instead of the bundled should work fine as long as it is newer than the V1.0 pre-release. To do so remove the RocketPy folder.


### OpenRocket
RocketPy doesn't simulate everything and is a bit barebones so the OpenRocket simulation is provided as well. This contains all parts and their relative positions. It is also how we got the dynamic stability margin since RocketPy doesn't evaluate it.