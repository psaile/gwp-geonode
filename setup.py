import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="gwp_geonode",
    version="0.2",
    author="",
    author_email="",
    description="gwp_geonode, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="gwp_geonode geonode django",
    url='https://github.com/gwp_geonode/gwp_geonode',
    packages=['gwp_geonode',],
    include_package_data=True,
    zip_safe=False,
)
