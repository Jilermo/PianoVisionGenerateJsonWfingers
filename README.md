# PianoVisionGenerateJsonWfingers
 Simple script for PianoVision to automatically add finger position to Json from an XML with finger info.

 Use tutorial.

 This script shouldn´t use any external library for python.

 For this to work you will need a MusicXML file with finger position information of your song.
 My recommendation is to get a MIDI file (the project only works with MIDI files that have left and right-hand notes separated but it can be easily modified for MIDI with no note separation) and then send that MIDI file to Piano Vision then get the JSON generated and visit piano vision site to add finger position (https://piano-vision-fingering.web.app/), add just one finger info and then download the file. This is needed so that the necessary data is generated in the JSON to store the finger position. If you jump this step the script will fail. 

 After you have your JSON and your MIDI file, you will need an XML with finger position for the specific song. My recommendation is to use the absolutely amazing tool by marcomusy pianoplayer (this script is based on his program) (https://github.com/marcomusy/pianoplayer) to get your MIDI file and generate finger position for that specific MIDI file, pianoplayer will generate an XML file with finger positioning.

 After you have the XML with finger position and the JSON from piano vision, rename the XML to 'input.xml' and the JSON to 'input.json' and pray for everything to work, then run the python file. And after some time you should have an 'output.json' in the folder, rename this JSON to the original JSON name that you get from piano vision and replace it with the one in the headset and you should have a working song with finger positioning.

Some info about this script, its a very small script that the only thing it does is map the finger position from the XML you provide to the JSON file of pianovision, it needs to try and check all the notes so that they match up because for some reason piano vision and pianoplayer output sometimes notes in different order.

You are free to use this script and modify it as you see fit but I don't provide any warranty that it will work correctly.
