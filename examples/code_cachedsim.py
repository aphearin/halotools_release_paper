>>> from halotools.sim_manager import CachedHaloCatalog
>>> halocat = CachedHaloCatalog(simname='bolshoi', redshift=0.5)

View the first ten halos in the catalog
>>> print(halocat.halo_table[0:10])

Inspect some of the halo catalog metadata
>>> print(halocat.Lbox, halocat.particle_mass)
