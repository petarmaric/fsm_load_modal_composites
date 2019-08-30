from setuptools import setup, find_packages


setup(
    name='fsm_load_modal_composites',
    version='1.0.1',
    url='https://github.com/petarmaric/fsm_load_modal_composites',
    license='BSD',
    author='Petar Maric',
    author_email='petarmaric@uns.ac.rs',
    description='Python library that loads modal composites from the file '\
                'containing the parametric model of buckling and free '\
                'vibration in prismatic shell structures, as computed by the '\
                'fsm_eigenvalue project.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    platforms='any',
    py_modules=['fsm_load_modal_composites'],
    install_requires=open('requirements.txt').read().splitlines(),
)
