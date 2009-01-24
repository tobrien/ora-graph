#   Copyright 2005 Tim O'Brien
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import os, ClientCookie, time
import xml.dom.minidom
import xml.parsers.expat

def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

class RelationGrabber:
    def __init__(self, uids, name, uid, f, level, maxlevel, opener, foafURL):
        self.uids = uids;
        self.uid = uid;
        self.f = f;
        self.level = level;
        self.maxlevel = maxlevel;
        self.opener = opener;
        self.foafURL = foafURL;
        self.name = name;
    
    def addRelations(self):
        print self.uid
        print self.uids.has_key( self.uid )
        if self.uids.has_key( self.uid ):
            print "Already Got it"
            return
        if self.level > self.maxlevel:
            print "Level Exceeded"
            return
        print "fetching " + self.uid
        self.uids.put( self.uid )
        try:
            doc = self.opener.open(self.foafURL + self.uid).read();
            # This pause is here to give the O'Reilly server a break
            time.sleep(1);
        except:
            print "Error retrieving"
            return
        try:
            personDom = xml.dom.minidom.parseString( doc )
        except:
            print "Error parsing"
            return
        subPerson = personDom.getElementsByTagName("foaf:Person")[0];
        subPersonNick = getText( subPerson.getElementsByTagName("foaf:nick")[0].childNodes );
        subPersonKnows = subPerson.getElementsByTagName( "foaf:knows" );
        for subElement in subPersonKnows:
            subsubPerson = subElement.getElementsByTagName("foaf:Person")[0];
            subName = getText( subsubPerson.getElementsByTagName("foaf:name")[0].childNodes );    
            subHomepage = subsubPerson.getElementsByTagName("homepage")[0].getAttribute('rdf:resource')    
            subUid = subHomepage.split('=')[1]
            self.f.write( '\t"' + self.name.replace('"', '\'').encode("utf-8") + '" -- "' + subName.replace('"', '\'').encode("utf-8") + '";\n' );
            grabber = RelationGrabber( self.uids, subName, subUid, self.f, self.level + 1, self.maxlevel, self.opener, self.foafURL )
            grabber.addRelations()
        
class UidCache:
    def __init__(self):
        self.uids = {};

    def put( self, uid ):
        self.uids[uid] = 1

    def has_key( self, uid ):
        return self.uids.has_key( uid );
