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

# Debug (1 debug http, 0 no debug) - if you are having network issues
debug=0

# How many levels to gather, this gathers two degrees of separation.
# DO NOT raise  this above 3- at the 4-th level of separation, you
# end up walking the entire O'Reilly database, and your script will
# execute for a few days.
maxLevel=2

# This is the central user id, for your graph.  You can figure out what your
# Connection user id is by looking at your own FOAF XML
centralUserId="374"
rootDudeNick="Tim O'Brien"

# Again, this is my lazy mechanism for logging into O'Reilly Connection
# from a Python script.  Remember, I warned you that this wasn't a pretty
# script, and this is the ugliest part.
cookiesFile="/home/tobrien/.mozilla/default/cz37fy41.slt/cookies.txt"

# Why? Alright, let me explain this.  We piggyback on your Firefox cookies,
# for this to work, log into O'Reilly Connection and your browser
urlPrefix="http://connection.oreilly.com"

foafURL=urlPrefix + "/users/connections.foaf.xml.php?user_id="

# authURL is strange - we go to auth.php but we also pass in the
# path that we want to be redirected to.  Not very RESTful.
authURL=urlPrefix + "/auth.php?returl=%2Fusers%2Fconnections.foaf.xml.php%3Fuser_id%3D" + centralUserId

outputFile="foaf.neato"         
preamble="""
graph G {
    size="7.5,10";
    tratio=fill;
    node[shape=point];
"""
epilouge="""
}
"""
