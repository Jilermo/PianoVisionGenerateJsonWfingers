# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 01:44:21 2023

@author: jiler
"""

import json
import xml.etree.ElementTree as ET

# Opening JSON file
f = open('inputjson.json')
# returns JSON object as 
# a dictionary
data = json.load(f)

class XmlNote:
  def __init__(self, pitch, octave, alter, finger):
    self.pitch = pitch
    self.octave = octave
    self.alter = alter
    self.finger=finger
    
    
def getNextPitch(XmlNote):
    _xmlNote=XmlNote
    if(_xmlNote.pitch=="A"):
        _xmlNote.pitch="G"
    elif(_xmlNote.pitch=="B"):
        _xmlNote.pitch="A"
    elif(_xmlNote.pitch=="C"):
        _xmlNote.pitch="B"
    elif(_xmlNote.pitch=="D"):
        _xmlNote.pitch="C"
    elif(_xmlNote.pitch=="E"):
        _xmlNote.pitch="D"
    elif(_xmlNote.pitch=="F"):
        _xmlNote.pitch="E"
    elif(_xmlNote.pitch=="G"):
        _xmlNote.pitch="F"
        _xmlNote.octave=1
    _xmlNote.alter=1
    return _xmlNote

xmlNotesRight=[]
xmlNotesRightMod=[]

xmlNotesLeft=[]
xmlNotesLeftMod=[]

octave2=0
step2="z"
alter2=0  
finger2=0
complete2=0

#opening xml
tree = ET.parse('input.xml')
root = tree.getroot()
x1=root[0]
x2=root[1]
x3=root[2]
x4=root[5]
if len(root)==5:
    print("two hands detected")

for notes in root[4].iter('note'):
    print(notes.tag)
    if (len(notes.findall('pitch'))>0):
        if(len(notes.findall('pitch')[0].findall('step'))>0):
            print(notes.findall('pitch')[0].findall('step')[0].text)
            step=notes.findall('pitch')[0].findall('step')[0].text
            octave=notes.findall('pitch')[0].findall('octave')[0].text
            alter=0
            if len(notes.findall('pitch')[0].findall('alter'))>0:
                print(notes.findall('pitch')[0].findall('alter')[0].text)
                alter=notes.findall('pitch')[0].findall('alter')[0].text
            finger=0
            notations=notes.findall('notations')
            if(len(notations)>0):
                if(len(notations[0].findall('technical'))>0):    
                    if len(notes.findall('notations')[0].findall('technical')[0].findall('fingering'))>0:
                        print(notes.findall('notations')[0].findall('technical')[0].findall('fingering')[0].text)
                        finger=notes.findall('notations')[0].findall('technical')[0].findall('fingering')[0].text
            xmlNotesRight.append(XmlNote(step,octave,alter,finger)) 
            
for notes in root[5].iter('note'):
    print(notes.tag)
    if (len(notes.findall('pitch'))>0):
        if(len(notes.findall('pitch')[0].findall('step'))>0):
            print(notes.findall('pitch')[0].findall('step')[0].text)
            step=notes.findall('pitch')[0].findall('step')[0].text
            octave=notes.findall('pitch')[0].findall('octave')[0].text
            alter=0
            if len(notes.findall('pitch')[0].findall('alter'))>0:
                print(notes.findall('pitch')[0].findall('alter')[0].text)
                alter=notes.findall('pitch')[0].findall('alter')[0].text
            finger=0
            notations=notes.findall('notations')
            if(len(notations)>0):
                if(len(notations[0].findall('technical'))>0):    
                    if len(notes.findall('notations')[0].findall('technical')[0].findall('fingering'))>0:
                        print(notes.findall('notations')[0].findall('technical')[0].findall('fingering')[0].text)
                        finger=notes.findall('notations')[0].findall('technical')[0].findall('fingering')[0].text
            xmlNotesLeft.append(XmlNote(step,octave,alter,finger)) 
            
'''
for child in root[4]:
    for j in child:          
        for k in j:             
            if k.tag=="notations":
                
                for l in k:
                    if l.tag=="technical":
                        finger2=l[0].text
                        #print("fingerinfo")
                        #print(finger2)
                        complete2+=1
                pass
            if k.tag=="pitch":                
                complete2+=1
                for l in k:                    
                    if (l.tag=="step"):
                        step2=l.text
                    if (l.tag=="alter"):
                        alter2=l.text
                    if (l.tag=="octave"):
                        octave2=l.text
            
            if(complete2==2):
                print(finger2)
                xmlNotes.append(XmlNote(step2,octave2,alter2,finger2))                
                print(xmlNotes[-1].finger)
                complete2=0
                finger2=0
'''    

#xmlNotes[0].finger=1
#print(xmlNotes[27].finger)
#print(xmlNotes[1])
xmlNotesRightMod=xmlNotesRight

for i in xmlNotesRightMod:
    #print(i.alter)
    if(i.alter==("-1")):
        i=getNextPitch(i)
        #print(i.octave)
        #print(i.pitch)
        
xmlNotesLeftMod=xmlNotesLeft
for i in xmlNotesLeftMod:
    #print(i.alter)
    if(i.alter==("-1")):
        i=getNextPitch(i)
        #print(i.octave)
        #print(i.pitch)
        

 
# Iterating through the json
# list
#data['tracksV2']['right']
##print(right[0]['notes'][0])
for i in range(len(data['tracksV2']['right'])):
    for j in range(len(data['tracksV2']['right'][i]['notes'])):
        pass
        #print(right[i]['notes'][j]['notePitch'])
        octave=0
        step="z"
        alter=0
        step=data['tracksV2']['right'][i]['notes'][j]['notePitch']
        octave=data['tracksV2']['right'][i]['notes'][j]['octave']
        
        #print(right[i]['notes'][j]['finger'])
        xmlNote3=XmlNote(step,octave,alter,0)
        if "#" in step:
            xmlNote3.pitch=step[0]
            xmlNote3.alter=1
        toremove=0
        for k in xmlNotesRightMod:
            if(xmlNote3.pitch == k.pitch and str(xmlNote3.octave) == str(k.octave) and str(xmlNote3.alter)== str(k.alter)):
                pass
                print(k.finger)
                data['tracksV2']['right'][i]['notes'][j]['finger']=k.finger
                #print(data['tracksV2']['right'][i]['notes'][j]['finger'])
                toremove=xmlNotesRightMod.index(k)
                break        
        xmlNotesRightMod.remove(xmlNotesRightMod[toremove])
        
for i in range(len(data['tracksV2']['left'])):
    for j in range(len(data['tracksV2']['left'][i]['notes'])):
        pass
        #print(right[i]['notes'][j]['notePitch'])
        octave=0
        step="z"
        alter=0
        step=data['tracksV2']['left'][i]['notes'][j]['notePitch']
        octave=data['tracksV2']['left'][i]['notes'][j]['octave']
        
        #print(right[i]['notes'][j]['finger'])
        xmlNote3=XmlNote(step,octave,alter,0)
        if "#" in step:
            xmlNote3.pitch=step[0]
            xmlNote3.alter=1
        toremove=0
        for k in xmlNotesLeftMod:
            if(xmlNote3.pitch == k.pitch and str(xmlNote3.octave) == str(k.octave) and str(xmlNote3.alter)== str(k.alter)):
                pass
                print(k.finger)
                data['tracksV2']['left'][i]['notes'][j]['finger']=6-int(k.finger)
                #print(data['tracksV2']['right'][i]['notes'][j]['finger'])
                toremove=xmlNotesLeftMod.index(k)
                break        
        xmlNotesLeftMod.remove(xmlNotesLeftMod[toremove])

# Serializing json
json_object = json.dumps(data)
 
# Writing to sample.json
with open("output.json", "w") as outfile:
    outfile.write(json_object)   

# Closing file
f.close()



        
    
    
