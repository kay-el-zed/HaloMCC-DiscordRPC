import authenticate, Rich_Presence, removetoken, os, time, xbox, sys, ui
# From One response 2 Factor does work
# removetoken.createToken()
# authenticate.main()
# Rich_Presence.main()
# removetoken.main()
ui.splashScreen()
selection = "a"
while(selection != None or selection != 5):
    selection = ui.UI()
    ui.option(selection)