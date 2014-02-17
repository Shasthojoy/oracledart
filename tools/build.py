#!/usr/bin/python

import platform
import subprocess
import os
import sys

def Main():
    userhome = os.path.expanduser("~")
    platformid = platform.system()
    env = os.environ.copy()
    if platformid == "Linux":
        env["ORACLE_OCI_HOME"] = "%s/Downloads/instantclient_11_2/sdk" % userhome
        env["ORACLE_OCCI_LIB_HOME"] = "%s/Downloads/instantclient_11_2" % userhome
        buildCommand = ['make', '-j', '8']
        extensionlibrary = "out/Debug/lib.target/liboracledart_extension.so"
    elif platformid == "Darwin":
        ORACLE_OCCI_LIB_HOME = "%s/Downloads/instantclient_11_2-2" % userhome
        subprocess.call(
            ["ln",
             "%s/libocci.dylib.11.1" % ORACLE_OCCI_LIB_HOME,
             "%s/libocci.dylib" % ORACLE_OCCI_LIB_HOME])
        subprocess.call(
            ["ln",
             "%s/ORACLE_OCCI_LIB_HOME/libclntsh.dylib.11.1" % ORACLE_OCCI_LIB_HOME,
             "%s/libclntsh.dylib" % ORACLE_OCCI_LIB_HOME])
        env["ORACLE_OCI_HOME"] = "%s/Downloads/instantclient_11_2/sdk" % userhome
        env["ORACLE_OCCI_LIB_HOME"] = ORACLE_OCCI_LIB_HOME
        buildCommand = ['xcodebuild',
                '-project', 'oracledart.xcodeproj',
                '-configuration', 'ReleaseIA32',
                'SYMROOT=%s/../dart/xcodebuild' % os.getcwd()]
        extensionlibrary = (
            "../dart/xcodebuild/ReleaseIA32/liboracledart_extension.dylib")
    elif platformid == "Windows" or platformid == "Microsoft":
        if not "JAVA_HOME" in env:
            print "JAVA_HOME is not set up"
            return 3
        env["ORACLE_OCI_HOME"] = (
            "%s\\downloads\\instantclient-sdk-nt-12.1.0.1.0\\instantclient_12_1\\sdk" %
            userhome)
        buildCommand = ['devenv',
                'oracledart.sln',
                '/build',
                'ReleaseIA32']
        extensionlibrary = (
            "..\\dart\\build\\ReleaseIA32\\oracledart_extension.dll")
    else:
        print "Unsupported platform"
        return 1

    print " ".join(buildCommand)
    process = subprocess.Popen(buildCommand, stdin=None, env=env)
    process.wait()
    print "Completed with %d" % (process.returncode)
    if process.returncode == 0:
        if platformid == "Linux" or platformid == "Darwin":
            subprocess.call("cp %s ." % (extensionlibrary), shell=True)
        else:
            subprocess.call(["copy", extensionlibrary, "."], shell=True)
    return process.returncode

if __name__ == '__main__':
    sys.exit(Main())
