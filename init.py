import nuke
import os, os.path

# ENVIRONMENT VARIABLES
nuke_path = os.getenv( 'NUKE_PATH' )

# INFO FEEDBACK
feedback = ' Custom tools from ' + nuke_path 
liner = '-'
for i in range( 0, len( feedback ) ):
	liner += '-'
print( '' )
print( liner )
print( feedback )
print( liner )
print( '' )

# PATHS
nuke.pluginAddPath( nuke_path.replace( '\\', '/' ) + '/gizmos' )
nuke.pluginAddPath( nuke_path.replace( '\\', '/' ) + '/icons' )
nuke.pluginAddPath( nuke_path.replace( '\\', '/' ) + '/plugins' )
nuke.pluginAddPath( nuke_path.replace( '\\', '/' ) + '/scripts' )

# PACKS
nuke.pluginAddPath( nuke_path.replace( '\\', '/' ) + '/gizmos/pixelfudger' )

# CRYPTOMATTE
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()
