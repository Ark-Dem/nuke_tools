import nuke
import os.path, subprocess


########################################################################################################################
# OPEN WINDOWS FOLDER FOR EACH SELECTED READ AND WRITE NODE
def ark_browseSelected():
	selList = nuke.selectedNodes()

	if selList != []:
		for each in selList:
			if each.Class() == 'Read' or each.Class() == 'Write':
				filePath = each.knob( 'file' ).getValue()
				dirPath = filePath[:filePath.rfind( '/' )+1]
				if os.path.exists( dirPath ):
					subprocess.Popen( 'explorer "' + dirPath.replace( '/', '\\' ) + '"' )

########################################################################################################################
# SET PROJECT FRAME RANGE AND FORMAT FROM SELECTED READ NODE

def ark_projRangeFromRead():
	selList = nuke.selectedNodes()

	if selList != []:
		if selList[0].Class() == 'Read':
			nuke.toNode( 'root' ).knob( 'first_frame' ).setValue( selList[0].knob( 'first' ).value() )
			nuke.toNode( 'root' ).knob( 'last_frame' ).setValue( selList[0].knob( 'last' ).value() )
			nuke.toNode( 'root' ).knob( 'format' ).setValue( selList[0].knob( 'format' ).value() )

########################################################################################################################
