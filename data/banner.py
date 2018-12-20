
# ------ Banner ------

import random

header1 = ''' \033[1;33m

   ██╗      ███╗  ██████╗██╗██╗   ████╗ ██╗ ██╗██████╗██╗    ██╗
   ██║    ██╔═╝██╗╚██╔══╝╚███╔╝  ██╔══█╗██║ ██║██╔═══╝██║    ██║
   ██║    ███████║ ╚██╗   ╚█╔╝   ╚═██╗╚╝██████║████╗  ██║    ██║
   ██║    ██╔══██║  ╚██╗   █║    █╗ ╚██╗██╔═██║██╔═╝  ██║    ██║
   ██████╗██║  ██║██████╗  ██╗   ╚████╔╝██║ ██║██████╗██████╗██████╗
   ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═╝    ╚═══╝ ╚═╝ ╚═╝╚═════╝╚═════╝╚═════╝
   
\033[1;m'''

header2 = ''' \033[1;32m

   #######################################################################
   #<><><><><><><><><><><><><><><..><><..><><..><><><><><><><><><><><><><#
   #>@@     @@@  @@@@ @@   @@.  .  .  .  .  . @@@  @@ @@  @@@@ @@   @@  <#
   #<@@    @@ @@ @@    @   @  ..    ..    .. @@ @@ @@ @@  @@@@ @@   @@  >#
   #>@@    @@ @@  @     @ @                   @    @@ @@  @@   @@   @@  <#
   #<@@    @@@@@   @     @     {LazyShell}     @   @@@@@  @@@  @@   @@  >#
   #>@@    @@ @@    @    @                      @  @@@@@  @@   @@   @@  <#
   #<@@@@  @@ @@    @@   @     ..    ..    ..@@ @@ @@ @@  @@@@ @@@@ @@@@>#
   #>@@@@  @@ @@ @@@@@   @@.  .  .  .  .  .   @@@  @@ @@  @@@@ @@@@ @@@@<#
   #><><><><><><><><><><><><..><><..><><..><><><><><><><><><><><><><><><>#
   #######################################################################

\033[1;m'''

def header():
    return random.choice([header1, header2])