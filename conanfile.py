#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostContainerConan(base.BoostBaseConan):
    name = "boost_container"
    url = "https://github.com/bincrafters/conan-boost_container"
    lib_short_names = ["container"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_intrusive",
        "boost_move",
        "boost_static_assert",
        "boost_type_traits"
    ]
