import pip
from pip._internal.utils.misc import get_installed_distributions
installed_packages = pip._internal.utils.misc.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
