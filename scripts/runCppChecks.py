#! /usr/bin/python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#<header>
#
#  <project>Bullet3</project>
#
# <description>
#  Python script used to run all of the Bullet cppcheck analysis
# </description>
#
#</header>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Standard imports

import os
import platform
import optparse
import subprocess
from os.path import *

# Local imports
import sys

BulletPath = os.environ[ "BULLET" ]


CppCheckPaths = \
   [ \
   "src",

   ]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Description:
#
# sgPrime ~ Run a single check on an sgPrime package
#
# Throw(s):
#
#      Exception - Failed running check

def CheckPackage( srcPath ):
   print "CPP_CHECK_PACKAGE : " , srcPath
   try:
   # Insure results path exists
      resultsPath =  BulletPath + "/results"
      if not exists( resultsPath ):
         os.mkdir( resultsPath )
         
    # Get package name
      indx = srcPath.rfind("/")
      pkg = srcPath[indx+1:]
      print "C++ Check : ", srcPath

   # Form XML output file for cppcheck
      xmlOutputFile = BulletPath + "/results/cppcheck-results-"+pkg+".xml"
      print "XML Output : ",xmlOutputFile
      
      pkg_path = "$BULLET/" + srcPath

   # Form command
      command = "/usr/bin/cppcheck --xml --enable=style --enable=portability --force -j 8 "
      command += " --library=std.cfg "
      command += " --suppress=preprocessorErrorDirective "
      command += " --suppress=variableScope "
      command += " --suppress=unusedStructMember "
      command += "-I$BULLET/src -I. --verbose --quiet -D__unix -D_SIGNAL_H "
      command += pkg_path
      command += " 2> " + xmlOutputFile
      print "CppCheck Command: "
      for tok in command.split(" "):
         print "\t",tok
      print
      sys.stdout.flush()

   # Execute command
      subprocess.call(command, shell=True)

   except(subprocess.CalledProcessError), e:
      raise Exception( "Subprocess Call Failed : " + str( e.cmd ) + " Returned error: " + str( e.returncode ) )
   except(Exception), e:
      raise e
   except:
      raise
   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Description:
#
# sgPrime ~ Run all unit tests
#
# Throw(s):
#
#   None, all errors cause an exit
#

def RunAllChecks():

   # Execute all checks in the path list
   for path in CppCheckPaths:
      CheckPackage( path )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main program

def main():

   
# Print cppcheck version...
   command = "cppcheck --version"
   subprocess.call( command, shell=True)

# Setup SGPRIME environment space
   try:
      if ( platform.system() == "Linux" ):
         os.putenv( 'LD_LIBRARY_PATH', os.environ['LD_LIBRARY_PATH'] + ':' + BulletPath +  '/lib' )
      elif( platform.system() == "Windows" ):
         os.putenv( 'PATH', os.environ['PATH'] + ';' + BulletPath +  '/lib' )
         os.environ[ 'SGPRIME' ] = BulletPath
   except Exception as err:
      print "An error occured: "
      print type( err )
      print err
      sys.exit( -1 )
   except:
      print "Unknown error "
      sys.exit( -1  )

# Run the whole shabang
   RunAllChecks()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The if __name__ == "__main__": ... trick exists in Python so that our Python files can act
# as either reusable modules, or as standalone programs. If this script is being executed by
# the python interpreter then it will evaluate to true. If the module functions are being
# called by an external program, it will evaluate to false

if __name__ == '__main__':
   main()


