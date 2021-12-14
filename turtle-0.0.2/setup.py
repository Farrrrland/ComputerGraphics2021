#!/usr/bin/env python

# Copyright (c) 2008-2009 Adroll.com, Valentino Volonghi.
# See LICENSE for details.

"""
Distutils installer for turtle.
"""

try:
    # Load setuptools, to build a specific source package
    import setuptools
except ImportError:
    pass

# For great justice, take off every zig.
import sys, os, pprint, traceback

import turtle
version = turtle.__version__

install_requires = ["Twisted>=8.0.1", "PyYAML>=3.0.8"]

setup = setuptools.setup
find_packages = setuptools.find_packages

# Most of the following code is from Divmod Epsilon, (C) 2008 Divmod, Inc.
# under MIT license, see http://divmod.org/trac/wiki/DivmodEpsilon
# since I only need this to install turtle correctly with Twisted
# Plugins I'd rather copy this few lines than actually add another
# dependency. Also this version uses the setuptools setup() function.

def pluginModules(moduleNames):
    from twisted.python.reflect import namedAny
    for moduleName in moduleNames:
        try:
            yield namedAny(moduleName)
        except ImportError:
            pass
        except (ValueError, ve):
            if ve.args[0] != 'Empty module name':
                traceback.print_exc()
        except:
            traceback.print_exc()

def _regeneratePluginCache(pluginPackages):
    ## print 'Regenerating cache with path: ',
    ## pprint.pprint(sys.path)
    from twisted import plugin
    for pluginModule in pluginModules([
        p + ".plugins" for p in pluginPackages]):
        # Not just *some* zigs, mind you - *every* zig:
        #print 'Full plugin list for %r: ' % (pluginModule.__name__)
        list(plugin.getPlugins(plugin.IPlugin, pluginModule))

def regeneratePluginCache(dist, pluginPackages):
    if 'install' in dist.commands:
        sys.path.insert(0, os.path.abspath(dist.command_obj['install'].install_lib))
        _regeneratePluginCache(pluginPackages)

def autosetup(**kw):
    packages = []
    datafiles = {}
    pluginPackages = []

    for (dirpath, dirnames, filenames) in os.walk(os.curdir):
        dirnames[:] = [p for p in dirnames if not p.startswith('.')]
        pkgName = dirpath[2:].replace('/', '.')
        if '__init__.py' in filenames:
            # The current directory is a Python package
            packages.append(pkgName)
        elif 'plugins' in dirnames:
            # The current directory is for the Twisted plugin system
            pluginPackages.append(pkgName)
            packages.append(pkgName)

    for package in packages:
        if '.' in package:
            continue
        D = datafiles[package] = []
        #print 'Files in package %r:' % (package,)
        #pprint.pprint(os.listdir(package))
        for (dirpath, dirnames, filenames) in os.walk(package):
            dirnames[:] = [p for p in dirnames if not p.startswith('.')]
            for filename in filenames:
                if filename == 'dropin.cache':
                    continue
                if (os.path.splitext(filename)[1] not in ('.py', '.pyc', '.pyo')
                    or '__init__.py' not in filenames):
                    D.append(os.path.join(dirpath[len(package)+1:], filename))
    autoresult = {
        'packages': packages,
        'package_data': datafiles,
        }
    #pprint.pprint(autoresult, indent=4)
    assert 'packages' not in kw
    assert 'package_data' not in kw
    kw.update(autoresult)
    distobj = setup(**kw)
    regeneratePluginCache(distobj, pluginPackages)
    return distobj

description = """\
Turtle is an HTTP proxy whose purpose is to throttle connections to
specific hostnames to avoid breaking terms of usage of those API
providers (like del.icio.us, technorati and so on).
"""

autosetup(
    name = "turtle",
    author = "Valentino Volonghi",
    author_email = "valentino@adroll.com",
    url = "http://adroll.com/labs",
    description = description,
    license = "MIT License",
    version=version,
    install_requires=install_requires,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet',
    ],
    include_package_data=True,
    zip_safe=False
)
