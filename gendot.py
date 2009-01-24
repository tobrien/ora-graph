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
import os, ClientCookie
import xml.dom.minidom
import xml.parsers.expat
from relation import RelationGrabber
from relation import UidCache

execfile('config.py')

# Set up the CookieJar to read from Mozilla
cookies = ClientCookie.MozillaCookieJar()
cookies.load(cookiesFile)

# Set the ClientCookie to DEBUG logging
if( debug == 1 ):
    logger = ClientCookie.getLogger("ClientCookie")
    logger.addHandler(ClientCookie.StreamHandler())
    logger.setLevel(ClientCookie.DEBUG)

# Configure an opening that knows about the refresh META 
opener = ClientCookie.build_opener(ClientCookie.HTTPCookieProcessor(cookies),
                                   ClientCookie.HTTPRefererProcessor,
                                   ClientCookie.HTTPEquivProcessor,
                                   ClientCookie.HTTPRefreshProcessor,
                                   ClientCookie.SeekableProcessor)

# conv method for getting text content
def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc


# Get the Root Dude
doc = opener.open( authURL ).read(  )
dom = xml.dom.minidom.parseString(doc)
rootDude = dom.getElementsByTagName("foaf:Person")[0];
rootDudeNick = getText( rootDude.getElementsByTagName("foaf:nick")[0].childNodes );

# Open the dot file
f=open(outputFile, 'w')
f.write( preamble );
uids = UidCache()

knows = rootDude.getElementsByTagName( "foaf:knows" );
for element in knows:
    person = element.getElementsByTagName("foaf:Person")[0];
    name = getText( person.getElementsByTagName("foaf:name")[0].childNodes );    
    homepage = person.getElementsByTagName("homepage")[0].getAttribute('rdf:resource')    
    uid = homepage.split('=')[1]
    print name;
    print uid;
    f.write( '\t"' + rootDudeNick.replace('"', '\'').encode("utf-8") + '" -- "' + name.replace('"', '\'').encode("utf-8") + '";\n' );
    grabber = RelationGrabber( uids, name, uid, f, 1, 3, opener, foafURL );
    grabber.addRelations()

f.write( epilouge );    

f.close();
