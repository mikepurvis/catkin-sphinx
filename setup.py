#!/usr/bin/env python

from distutils.core import setup

setup(name='catkin-sphinx',
      version='0.1.0',
      packages=['catkin_sphinx'],
      package_data = {'catkin_sphinx': ['theme/ros-theme/theme.conf',
                                        'theme/ros-theme/static/sphinxdoc.css',
                                        'theme/ros-theme/static/pygments.css']},
      package_dir = {'catkin_sphinx': 'src/catkin_sphinx'},
      author = "Troy Straszheim", 
      author_email = "straszheim@willowgarage.com",
      url = "http://www.ros.org/",
      download_url = "http://pr.willowgarage.com/downloads/catkin_sphinx/", 
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python", 
        "License :: OSI Approved :: BSD License" ],
      description = "ROS package library", 
      long_description = """\
Sphinx extension for Catkin projects
""",
      license = "BSD"
      )

