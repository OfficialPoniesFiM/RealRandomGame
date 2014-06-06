#Setup file for my game, RandomGame.
#RandomGame got ported to 2.7 because of compatibility.

from distutils.core import setup
import py2exe

setup(console=["main_python27.py"],
      windows=["main_python27.py"],
      name="RandomGame",
      version='1.0',
      description='A random game.'
      options={
          "py2exe": {
              "packages": ["pygame"],
              "excludes": ['doctest', 'pdb', 'unittest', 'difflib', 'inspect'],
              "bundle_files": 1,
              "optimize": 1,
              "dist_dir": "exeFinal27"
              }
          }
      )
