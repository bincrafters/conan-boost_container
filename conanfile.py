from conans import ConanFile, tools, os

class BoostContainerConan(ConanFile):
    name = "Boost.Container"
    version = "1.64.0"
    generators = "txt" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/boostorg/container"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "container"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing" 
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Functional/1.64.0@bincrafters/testing", \
                      "Boost.Intrusive/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing"

                      #assert1 config0 core2 functional5 intrusive6 move3 static_assert1 type_traits3

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

