import nuke
import scripts
import pixelfudger

# VARIABLES
projPaths = { 'P:/relicts/comp':'/comp/_nk' }

# DEFS
def incrSceneOnChange():
	nukescripts.script_and_write_nodes_version_up()

# TOOLBARS
tb = nuke.toolbar( 'Nodes' )

cust_tb = tb.addMenu( 'Relicts', 'relicts.png' )
cust_tb.addCommand( 'Slate', 'nuke.createNode( "ark_slate", "facilityname \\\"RELICTS\\\"" )', 'ctrl+alt+s' )
cust_tb.addCommand( 'Depth Fog', 'nuke.createNode( "ark_depthFog" )' )
cust_tb.addCommand( 'Depth Slice', 'nuke.createNode( "ark_depthSlice" )' )
cust_tb.addCommand( 'Eyes Grade', 'nuke.createNode( "ark_eyesGrade" )' )
cust_tb.addCommand( 'Compare Channels Node', 'nuke.createNode( "ark_compareChannels" )' )
cust_tb.addCommand( 'NaN|Inf Remover', 'nuke.createNode( "ark_deNanInf" )' )
cust_tb.addCommand( 'Multi-Step Blur', 'nuke.createNode( "MultiStepBlur" )' )
cust_tb.addCommand( 'Scanline Wipe', 'nuke.createNode( "ark_scanWipe" )' )
cust_tb.addCommand( 'SliceTool', 'nuke.createNode( "SliceTool" )' )
cust_tb.addCommand( 'Point Position Mask', 'nuke.createNode( "PointPositionMask" )' )
cust_tb.addSeparator()
cust_tb.addCommand( 'Open Explorer for Selected', 'scripts.ark_browseSelected()', 'ctrl+e' )
cust_tb.addCommand( 'Frame Range from Selected Read', 'scripts.ark_projRangeFromRead()', 'shift+alt+r' )
cust_tb.addSeparator()
cust_tb.addCommand( 'Start Scene Increment on Change', 'nuke.addUpdateUI( incrSceneOnChange )' )
cust_tb.addCommand( 'End Scene Increment on Change', 'nuke.removeUpdateUI( incrSceneOnChange )' )

# FAVOURITES
favDirs = {}
for eachProjPath in projPaths:
	if os.path.exists( eachProjPath ):
		shots = os.listdir( eachProjPath )
		for eachShot in shots:
			if os.path.isdir( eachProjPath + '/' + eachShot ):
				favDirs[ eachShot ] = eachProjPath + '/' + eachShot + projPaths[ eachProjPath ]

favShots = list( favDirs.keys() )
favShots.sort()

for eachShot in favShots:
	nuke.addFavoriteDir( eachShot, favDirs[ eachShot ], 0 )

# IMAGE FORMATS
nuke.addFormat( ' 1920 818 1.0 HD_2.35 ' )
nuke.addFormat( ' 1080 1350 1.0 Instagram_Video ' )
nuke.addFormat( ' 1080 1920 1.0 Instagram_Story ' )
nuke.addFormat( ' 864 1080 1.0 Instagram_Post ' )
nuke.addFormat( ' 640 640 1.0 Facebook_Video ' )
nuke.addFormat( ' 860 484 1.0 Artstation_Blog ' )

# DEFAULTS
nuke.knob( 'preferences.postage_stamp_mode', 'Static frame' )
nuke.knob( 'preferences.viewer_bg_color_3D', '0x7f7f7fff' )

nuke.knobDefault( 'Root.fps', '24' )
nuke.knobDefault( 'Root.format', ' 1920 818 1.0 HD_2.35 ' )
nuke.knobDefault( 'Write.jpeg._jpeg_quality', '1' )
nuke.knobDefault( 'Write.exr.datatype', '16 bit half' )
nuke.knobDefault( 'Write.exr.compression', 'Zip (1 scanline)' )
nuke.knobDefault( 'Read.cached', '1' )

# CRYPTOMATTE
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()
