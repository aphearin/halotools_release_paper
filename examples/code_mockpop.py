>>> from halotools.sim_manager import CachedHaloCatalog
>>> halocat = CachedHaloCatalog(simname='bolshoi', redshift=0)

>>> from halotools.empirical_models import PrebuiltHodModelFactory
>>> model = PrebuiltHodModelFactory('leauthaud11')

>>> model.populate_mock(halocat)

View the first ten galaxies in the catalog
>>> print(model.mock.galaxy_table[0:10])
