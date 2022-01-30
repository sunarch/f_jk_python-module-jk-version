

# from __future__ import annotations

import re
import os
import typing

from .Version import Version
from .BaseVersionConstraint import BaseVersionConstraint




class VersionConstraintLE(BaseVersionConstraint):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, version:Version):
		assert isinstance(version, Version)

		self.__v = version
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def check(self, version:Version) -> bool:
		assert isinstance(version, Version)

		return version <= self.__v
	#

	def toJSON(self) -> list:
		return [ "<=", str(self.__v) ]
	#

	def __str__(self):
		return "<={}".format(self.__v)
	#

	def __repr__(self):
		return "<={}".format(self.__v)
	#

#






