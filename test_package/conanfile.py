#  Copyright (c) 2022 Ultimaker B.V.
#  CuraEngine is released under the terms of the AGPLv3 or higher

from conan import ConanFile
from conan.tools.env import VirtualRunEnv
from conans import tools
from conans.errors import ConanException
from io import StringIO


class CuraEngineTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "VirtualRunEnv"

    def generate(self):
        venv = VirtualRunEnv(self)
        venv.generate()

    def build(self):
        pass

    def imports(self):
        self.copy("*.lib", dst = ".", src = "@bindirs")
        if self.settings.os == "Windows" and not tools.cross_building(self):
            self.copy("*.dll", dst = self.build_folder, src = "@bindirs")
            self.copy("*.dylib", dst = self.build_folder, src = "@bindirs")

    def test(self):
        print("not going to bother testing, am I an idiot?")
