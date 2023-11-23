import platform

# Output of current OS
print(platform.platform(True, True))
# Generic name of processor
print(platform.machine())
# Real name of processor
print(platform.processor())
# Generic name of OS
print(platform.system())

# Name of the Python implementation
print(platform.python_implementation())
# Python Version as tuple
print(platform.python_version_tuple())
