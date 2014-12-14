#this is a paintprogram for anyone to use. they can import and save images and using the tools, stamps, or themes, can creat
#their own pictures or edit current pictures.
from pygame import *
from random import *
screen=display.set_mode((1024,768))

init()                                  
mixer.music.load("Dragon Roost Island.mp3")      #paly music 
mixer.music.play(-1)

Wolf = image.load("pictures/wolf copy.png") 
screen.blit(Wolf,(0,0))

#####IMPORTANT!PLEASE WAIT THING

colour=(0,0,0)

clrs=[(0,0,0),(0,0,0)]  ##list of previous and current colour

colourspec = image.load("pictures/spectrum.jpg")
screen.blit(colourspec,(100,10))

font.init()
text = font.SysFont("Times New Roman", 20)

running=True
######################MX/MY POS###########################
posrect = Rect(830,80,100,25)
posback = screen.subsurface(posrect).copy()
######################TOOLS###############################
stampwolf = image.load("pictures/Stamp Stuff/stamp.png")
wolftool  = image.load("pictures/wolf copy1.png") 
specspraypic = image.load("pictures/specspray.png")
spectool = Rect(895,640,25,55)
spectoolpic = image.load("pictures/spectool.png")
coolrect = Rect(805,640,55,55)
coolrectpic = image.load("pictures/coolrect.png")
undorect = Rect(530,25,70,70)
undopic = image.load("pictures/Undo.png")
redorect = Rect(610,25,70,70)
redopic = image.load("pictures/Redo.png")
box="Tools"
toolrect=Rect(722,297,80,25)
thing=Rect(0,0,670,768)
floodfillrect=Rect(725,473,50,65)
paintbucketpic = image.load("pictures/paintbucketselected.png")
paintrect=Rect(725,345,50,50)
paintbrushpic = image.load("pictures/paintbrushselected.png")
eraserrect=Rect(895,345,50,50)
eraserpic = image.load("pictures/eraserselected.png")
canvas=Rect(35,110,620,630)        
pencilrect=Rect(820,345,35,50)
pencilpic = image.load("pictures/pencilselected.png")
saverect=Rect(450,25,70,70)
savepic = image.load("pictures/savepic.png")
loadrect = Rect(690,25,70,70)
loadpic = image.load("pictures/loadicon.jpg")
colourselect=Rect(730,415,45,45)
dropperpic = image.load("pictures/dropperselected.png")
linerect=Rect(878,407,57,52)
linepic = image.load("pictures/lineselected.png")
textrect=Rect(525,0,250,30)
specrect=Rect(100,10,324,87)
clearrect=Rect(800,415,52,50)
clearpic = image.load("pictures/clearselected.png")
spraypaintrect=Rect(820,473,35,65)
spraycanpic = image.load("pictures/spraypaintselected.png")
rectanglefilledrect=Rect(877,480,60,50)
rectfilledpic = image.load("pictures/solidrectselected.png")
rectangleemptyrect=Rect(735,560,50,50)
rectemptypic = image.load("pictures/emptysquareselected.png")
emptyelipserect=Rect(880,555,55,52)
emptyelipsepic = image.load("pictures/elipsedraw.png")
filledelipserect=Rect(800,560,60,50)
filledelipsepic = image.load("pictures/solidelipseselected.png")
trianglerect=Rect(735,640,55,55)
trianglepic = image.load("pictures/triangleselected.png")
######################STAMPTOOLS##################################
stamprect=Rect(802,297,80,25)
zeldarect=Rect(725,345,57,95)
zeldapic = image.load("pictures/Stamp Stuff/zeldasel.png")
triforcerect = Rect(790,345,160,95)
triforcepic = image.load("pictures/Stamp Stuff/triforcesel.png")
ganondorfrect=Rect(730,445,57,95)
ganondorfpic = image.load("pictures/Stamp Stuff/ganondorfsel.png")
linkrect = Rect(802,445,65,95)
linkpic = image.load("pictures/Stamp Stuff/linksel.png")
masterswordrect = Rect(880,460,65,70)
masterswordpic = image.load("pictures/Stamp Stuff/masterswordsel.png")
midnarect = Rect(730,550,95,80)
midnapic = image.load("pictures/Stamp Stuff/midnawolfsel.png")
eponarect = Rect(835,550,95,80)
eponapic = image.load("pictures/Stamp Stuff/linkhorsesel.png")
ocarinarect = Rect(780,640,85,60)
ocarinapic = image.load("pictures/Stamp Stuff/ocarinasel.png")
################THEMES#####################
themerect = Rect(882,297,80,25)
themepic = image.load("pictures/Theme Stuff/thememain.png")
theme1 = image.load("pictures/Theme Stuff/theme1.png")
theme2 = image.load("pictures/Theme Stuff/theme2.png")
theme3 = image.load("pictures/Theme Stuff/theme3.png")
theme4 = image.load("pictures/Theme Stuff/theme4.png")
theme5 = image.load("pictures/Theme Stuff/theme5.png")
theme6 = image.load("pictures/Theme Stuff/theme6.png")
theme7 = image.load("pictures/Theme Stuff/theme7.png")
theme8 = image.load("pictures/Theme Stuff/theme8.png")
theme1rect = Rect(725,345,108,95)
theme2rect = Rect(835,345,113,95)
theme3rect = Rect(725,450,108,75)
theme4rect = Rect(835,450,113,75)
theme5rect = Rect(725,540,108,65)
theme6rect = Rect(835,540,108,65)
theme7rect = Rect(725,625,108,80)
theme8rect = Rect(838,625,108,73)
theme1pic = image.load("pictures/Theme Stuff/theme1.jpg")
theme2pic = image.load("pictures/Theme Stuff/theme2.jpg")
theme3pic = image.load("pictures/Theme Stuff/theme3.jpeg")
theme4pic = image.load("pictures/Theme Stuff/theme4.jpg")
theme5pic = image.load("pictures/Theme Stuff/theme5.jpg")
theme6pic = image.load("pictures/Theme Stuff/theme6.jpeg")
theme7pic = image.load("pictures/Theme Stuff/theme7.jpg")
theme8pic = image.load("pictures/Theme Stuff/theme8.jpg")

##########STAMPS####################
zeldastamp = image.load("pictures/Stamp Stuff/Zelda.png")
linkstamp = image.load("pictures/Stamp Stuff/LinkStamp.png")
eponastamp = image.load("pictures/Stamp Stuff/EponaStamp.png")
ocarinastamp = image.load("pictures/Stamp Stuff/ocarina.png")
triforcestamp = image.load("pictures/Stamp Stuff/TriforceStamp.png")
midnastamp = image.load("pictures/Stamp Stuff/Midna_and_Wolf.png")
ganondorfstamp = image.load("pictures/Stamp Stuff/ganondorf.png")
masterswordstamp = image.load("pictures/Stamp Stuff/Master Sword Stamp.png")
####################DESCRIPTIONSTUFF###
pleasewait = image.load("pictures/Description Stuff/pleasewait.png")
please = image.load("pictures/Description Stuff/please.png")
specspraydes = image.load("pictures/Description Stuff/SpecSprayDes.png")
spectooldes = image.load("pictures/Description Stuff/Spec Tool.png")
paintdes = image.load("pictures/Description Stuff/paintbrush.png")
pencildes= image.load("pictures/Description Stuff/pencil.png")
eraserdes= image.load("pictures/Description Stuff/eraser.png")
dropperdes= image.load("pictures/Description Stuff/colourselect.png")
cleardes= image.load("pictures/Description Stuff/clear.png")
linedes= image.load("pictures/Description Stuff/linetool.png")
paintbucketdes= image.load("pictures/Description Stuff/paintbucket.png")
spraypaintdes= image.load("pictures/Description Stuff/spraypaint.png")
filledrectdes= image.load("pictures/Description Stuff/filledrect.png")
emptyrectdes= image.load("pictures/Description Stuff/emptyrect.png")
filledelipsedes= image.load("pictures/Description Stuff/filledelipse.png")
emptyelipsedes= image.load("pictures/Description Stuff/emptyelipse.png")
triangledes= image.load("pictures/Description Stuff/triangle.png")
coolrectdes= image.load("pictures/Description Stuff/coolrect.png")
welcome= image.load("pictures/Description Stuff/welcome.png")
tools= image.load("pictures/Description Stuff/tools.png")
stamps= image.load("pictures/Description Stuff/stamps.png")
themes= image.load("pictures/Description Stuff/themes.png")
zeldades =image.load("pictures/Description Stuff/zelda.png")
triforcedes =image.load("pictures/Description Stuff/triforce.png")
ganondorfdes =image.load("pictures/Description Stuff/ganondorf.png")
linkdes =image.load("pictures/Description Stuff/link.png")
mastersworddes =image.load("pictures/Description Stuff/mastersword.png")
midnades =image.load("pictures/Description Stuff/midna.png")
eponades =image.load("pictures/Description Stuff/epona.png")
ocarinades =image.load("pictures/Description Stuff/ocarina.png")
theme1des=image.load("pictures/Description Stuff/theme1.png")
theme2des=image.load("pictures/Description Stuff/theme2.png")
theme3des=image.load("pictures/Description Stuff/theme3.png")
theme4des=image.load("pictures/Description Stuff/theme4.png")
theme5des=image.load("pictures/Description Stuff/theme5.png")
theme6des=image.load("pictures/Description Stuff/theme6.png")
theme7des=image.load("pictures/Description Stuff/theme7.png")
theme8des=image.load("pictures/Description Stuff/theme8.png")
themeplease=image.load("pictures/Description Stuff/themeplease.png")
stampplease=image.load("pictures/Description Stuff/stampplease.png")
#######################################
undolist=[]
redolist=[]
##########LOAD/SAVE####################
def specspray(x,y,oc,nc):
    for i in range(size*2):  #draws faster the bigger the size
        rmx=randint(-1*(size+15),size+15)
        rmy=randint(-1*(size+15),size+15)
        dist=(((x-(x+rmx)))**2+(y-(y+rmy))**2)**0.5
        if canvas.collidepoint(rmx+x,rmy+y): #Crashes if the point isnt on thescreen
            if screen.get_at((rmx+x,rmy+y))==oc: #if its old colour 
                if dist < size:
                    screen.set_at((rmx+x,rmy+y),nc)
def spec(x,y,oc,nc):
    if screen.get_at((x,y))==oc:
        screen.set_at((x,y),nc)
        xdif=mx-omx
        ydif=my-omy
        dist=(xdif**2+ydif**2)**0.5
        if dist>0:
            for i in range(int(dist)):
                if screen.get_at((omx+int(i*xdif/dist),omy+int(i*ydif/dist)))==oc: #checks if its in the oldcolour before drawing it so it doesnt leak out the edges
                    screen.set_at((omx+int(i*xdif/dist),omy+int(i*ydif/dist)),nc)
def ffill(x,y,fc,rc):
    points = [(x,y)]
    if fc!=rc:
        while len(points) > 0:
            x,y = points.pop()
            if 0 < x < screen.get_width() and 0 < y < screen.get_height() and screen.get_at((x,y))[:3] == rc: #so it doesnt crash by going out of the screen
                screen.set_at((x,y),fc) #if pixles old colour, replace with new
                points += [(x + 1,y), (x - 1, y), (x, y + 1), (x, y - 1)]  #Goes through the 4 point around the pixle and ads to list
def getName():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    wholeback = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(700,110,200,25) # make changes here.

    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:           
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                else:
                    ans += chr(e.key)       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))        
        display.flip()
        
    screen.blit(wholeback,(0,0))
    return ans
comicFont = font.SysFont("Comic Sans MS", 20)

draw.rect(screen,(0,0,0),specrect,2)

tool="None"
stamp="None"
cooltool="None"
theme="None"

draw.rect(screen,(255,255,255),(35,110,620,630))
 
size=10 # default size
flag=False  #this flag is for pasting pleasewait, check out line 714 for explination
mx,my=mouse.get_pos()
mb=mouse.get_pressed()
textback=screen.subsurface(textrect).copy() # this blits over the text every time so its not a big blob.
edit = screen.subsurface(canvas).copy()
undolist.append(edit)
oldcolour=colour
screen.blit(wolftool,(688,194))
screen.blit(welcome,(697,119))
while running:
    if colour!=oldcolour:  #so it only adds a colour to the clr list when the colour changes
        clrs.append(colour)
        oldcolour=colour
    screen.blit(textback,(525,0))
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:   
           if evt.button == 1:
               ol=screen.get_at((mx,my))
               start = evt.pos
               canvasback=screen.subsurface(canvas).copy()
               thingback=screen.subsurface(thing).copy()
               posA,posB=mx,my
               colour = clrs[len(clrs)-1]
           if evt.button == 3:#right click to switch to previous colour
               colour = clrs[len(clrs)-2]
           if evt.button == 4:#Used this event for increasing size
               if size <96:
                   size += 5
           if evt.button == 5:#Used this event for increasing size
               if size > 6:
                   size -= 5
        if evt.type == MOUSEBUTTONUP:
####################UNDO/REDO#####################
            if canvas.collidepoint(mx,my) and evt.button == 1: #everytime i stop drawing it saves the image to my undo list
                edit = screen.subsurface(canvas).copy()
                undolist.append(edit)
            if undorect.collidepoint(mx,my):
                if len(undolist) > 1:    #so the empty canvas is always in the list
                    redolist.append(undolist[len(undolist)-1])  #adds undone item to the redo list
                    undolist.remove(undolist[len(undolist)-1])
                    screen.blit(undolist[len(undolist)-1],(35,110))
            if redorect.collidepoint(mx,my):
                if len(redolist) > 0:
                    screen.blit(redolist[len(redolist)-1],(35,110))  #ads the redone item to the undo list
                    undolist.append(redolist[len(redolist)-1])
                    redolist.remove(redolist[len(redolist)-1])

    txtPic = text.render("Your current draw size is:"+str(size), True, (255,255,255))
    screen.blit(txtPic,(650-txtPic.get_width()/2, 10-txtPic.get_height()/2))

    if canvas.collidepoint(mx,my):
        screen.blit(posback,(830,80))     # this blits over the text every time so its not a big blob.
        txtPic = text.render(str((mx,my)), True, (255,255,255))
        screen.blit(txtPic,(880-txtPic.get_width()/2, 90-txtPic.get_height()/2))
    
           
    omx,omy=mx,my        
    mx,my=mouse.get_pos()
    omb=mb
    mb=mouse.get_pressed()
##################################################
    draw.rect(screen,(0,0,0),canvas,1)
    draw.rect(screen,clrs[len(clrs)-1],(10,10,80,87))   ##shows current and previous colour being used
    draw.line(screen,clrs[len(clrs)-2],(8,10),(92,10),5)
    draw.line(screen,clrs[len(clrs)-2],(8,97),(92,97),5)
    draw.line(screen,clrs[len(clrs)-2],(10,10),(10,97),5)
    draw.line(screen,clrs[len(clrs)-2],(90,10),(90,97),5)
##################################################
    screen.blit(loadpic,(690,25))
    screen.blit(undopic,(530,25))
    screen.blit(redopic,(610,25))
    screen.blit(savepic,(450,25))
    if mb[0]==1 and saverect.collidepoint(mx,my): #image save
        txt = getName()
        image.save(screen.subsurface(canvas),txt+".bmp")           
###############LOADFILE###############################
    if mb[0]==1 and loadrect.collidepoint(mx,my):
        txt = getName()                     # this is how you would call my getName function
                                            # your main loop will stop looping until user hits enter
        loadedpic=image.load(txt+".bmp")
        screen.blit(loadedpic,(35,110))

###################################################### swtiches between the three main edditing options, tools, stamps, themes
    if mb[0]==1 and toolrect.collidepoint(mx,my):
        screen.blit(wolftool,(688,194))
        screen.blit(tools,(697,119))
        box="Tools"
        tool="None"
        stamp="None"
        cooltool="None"
        theme="None"
    if mb[0]==1 and stamprect.collidepoint(mx,my):
        screen.blit(stampwolf,(694,205))
        screen.blit(stamps,(697,119))
        box="Stamps"
        tool="None"
        stamp="None"
        cooltool="None"
        theme="None"
    if mb[0]==1 and themerect.collidepoint(mx,my):
        screen.blit(themepic,(686,199))
        screen.blit(themes,(697,119))
        box="Themes"
        tool="None"
        stamp="None"
        cooltool="None"
        theme="None"
#########THIS IS THE BEGINNING OF THEMES###########
    if box=="Themes":
        if mb[0]==1 and theme1rect.collidepoint(mx,my) and omb != mb: #the omb!=mb is so it can be unclicked and so if you drag your mouse from the canvas
            if theme=="Theme1":                                         #onto the tools thingy, it doesnt change
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme1"
                screen.blit(theme1,(686,199))
                screen.blit(theme1des,(697,119))
        if mb[0]==1 and theme2rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme2":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme2"
                screen.blit(theme2,(686,199))
                screen.blit(theme2des,(697,119))
        if mb[0]==1 and theme3rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme3":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme3"
                screen.blit(theme3,(686,199))
                screen.blit(theme3des,(697,119))
        if mb[0]==1 and theme4rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme4":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme4"
                screen.blit(theme4,(686,199))
                screen.blit(theme4des,(697,119))
        if mb[0]==1 and theme5rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme5":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme5"
                screen.blit(theme5,(686,199))
                screen.blit(theme5des,(697,119))
        if mb[0]==1 and theme6rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme6":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme6"
                screen.blit(theme6,(686,199))
                screen.blit(theme6des,(697,119))
        if mb[0]==1 and theme7rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme7":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme7"
                screen.blit(theme7,(686,199))
                screen.blit(theme7des,(697,119))
        if mb[0]==1 and theme8rect.collidepoint(mx,my) and omb != mb:
            if theme=="Theme8":
                theme="None"
                screen.blit(edit,(35,110))
                screen.blit(themepic,(686,199))
                screen.blit(themeplease,(697,119))
            else:
                theme="Theme8"
                screen.blit(theme8,(686,199))
                screen.blit(theme8des,(697,119))
        screen.set_clip(canvas)
        if theme=="Theme1":
            screen.blit(theme1pic,(35,110))
        if theme=="Theme2":
            screen.blit(theme2pic,(35,110))
        if theme=="Theme3":
            screen.blit(theme3pic,(35,110))
        if theme=="Theme4":
            screen.blit(theme4pic,(35,110))
        if theme=="Theme5":
            screen.blit(theme5pic,(35,110))
        if theme=="Theme6":
            screen.blit(theme6pic,(35,110))
        if theme=="Theme7":
            screen.blit(theme7pic,(35,110))
        if theme=="Theme8":
            screen.blit(theme8pic,(35,110))
        screen.set_clip(None)
#########THIS IS THE END OF THEMES#################
#########THIS IS THE BEGINNING OF STAMPS##########
    if box=="Stamps":
        if mb[0]==1 and zeldarect.collidepoint(mx,my) and omb!=mb:
            screen.blit(zeldapic,(694,205))
            screen.blit(zeldades,(697,119))
            stamp="Zelda"
        if mb[0]==1 and triforcerect.collidepoint(mx,my) and omb!=mb:
            screen.blit(triforcepic,(694,205))
            screen.blit(triforcedes,(697,119))
            stamp="Triforce"
        if mb[0]==1 and ganondorfrect.collidepoint(mx,my) and omb!=mb:
            screen.blit(ganondorfpic,(694,205))
            screen.blit(ganondorfdes,(697,119))
            stamp="Ganondorf"
        if mb[0]==1 and linkrect.collidepoint(mx,my) and omb!=mb:
            screen.blit(linkpic,(694,205))
            screen.blit(linkdes,(697,119))
            stamp="Link"
        if mb[0]==1 and masterswordrect.collidepoint(mx,my) and omb!=mb:
            screen.blit(masterswordpic,(694,205))
            screen.blit(mastersworddes,(697,119))
            stamp="Mastersword"
        if mb[0]==1 and midnarect.collidepoint(mx,my) and omb!=mb:
            screen.blit(midnapic,(694,205))
            screen.blit(midnades,(697,119))
            stamp="Midna"
        if mb[0]==1 and eponarect.collidepoint(mx,my) and omb!=mb:
            screen.blit(eponapic,(694,205))
            screen.blit(eponades,(697,119))
            stamp="Epona"
        if mb[0]==1 and ocarinarect.collidepoint(mx,my) and omb!=mb:
            screen.blit(ocarinapic,(694,205))
            screen.blit(ocarinades,(697,119))
            stamp="Ocarina"
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            redolist=[]      #Resets the Redo list when something new is being done
            if stamp=="Zelda":
                screen.blit(canvasback,(35,110))  #so when you drag the image it doesnt draw a billion zeldas until you let go
                screen.blit(zeldastamp,(mx-100,my-100))
            if stamp=="Link":
                screen.blit(canvasback,(35,110))
                screen.blit(linkstamp,(mx-100,my-100))
            if stamp=="Ocarina":
                screen.blit(canvasback,(35,110))
                screen.blit(ocarinastamp,(mx-100,my-100))
            if stamp=="Epona":
                screen.blit(canvasback,(35,110))
                screen.blit(eponastamp,(mx-100,my-100))
            if stamp=="Midna":
                screen.blit(canvasback,(35,110))
                screen.blit(midnastamp,(mx-200,my-200))
            if stamp=="Mastersword":
                screen.blit(canvasback,(35,110))
                screen.blit(masterswordstamp,(mx-100,my-100))
            if stamp=="Ganondorf":
                screen.blit(canvasback,(35,110))
                screen.blit(ganondorfstamp,(mx-100,my-100))
            if stamp=="Triforce":
                screen.blit(canvasback,(35,110))
                screen.blit(triforcestamp,(mx-100,my-50))
            screen.set_clip(None)
######THIS IS THE END OF STAMPS###########
######THIS IS THE BEGINNING OF TOOLS#######
    if box=="Tools":   
        if mb[0]==1 and spectool.collidepoint(mx,my) and omb != mb:
            if cooltool=="Spec Tool":
                cooltool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                cooltool="Spec Tool"
                tool="None"
                screen.blit(spectoolpic,(688,194))
                screen.blit(spectooldes,(697,119))
        if mb[0]==1 and coolrect.collidepoint(mx,my) and omb != mb:
            if tool=="Cool Rect":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                tool="Cool Rect"
                cooltool="None"
                screen.blit(coolrectpic,(688,194))
                screen.blit(coolrectdes,(697,119))
        if mb[0]==1 and trianglerect.collidepoint(mx,my) and omb != mb:
            if tool=="Triangle":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(trianglepic,(688,194))
                screen.blit(triangledes,(697,119))
                tool="Triangle"
                cooltool="None"
        if mb[0]==1 and filledelipserect.collidepoint(mx,my) and omb != mb:
            if tool=="Filled Elipse":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(filledelipsepic,(688,194))
                screen.blit(filledelipsedes,(697,119))
                tool="Filled Elipse"
                cooltool="None"
        if mb[0]==1 and emptyelipserect.collidepoint(mx,my) and omb != mb:
            if tool=="Empty Elipse":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(emptyelipsepic,(688,194))
                screen.blit(emptyelipsedes,(697,119))
                tool="Empty Elipse"
                cooltool="None"
        if mb[0]==1 and rectangleemptyrect.collidepoint(mx,my) and omb != mb:
            if tool=="Empty Rectangle":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(rectemptypic,(688,194))
                screen.blit(emptyrectdes,(697,119))
                tool="Empty Rectangle"
                cooltool="None"
        if mb[0]==1 and rectanglefilledrect.collidepoint(mx,my) and omb != mb:
            if tool=="Rectangle Filled":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(rectfilledpic,(688,194))
                screen.blit(filledrectdes,(697,119))
                tool="Rectangle Filled"
                cooltool="None"
        if mb[0]==1 and spraypaintrect.collidepoint(mx,my) and omb != mb:
            if tool=="Spray Paint" and cooltool!="Spec Tool" or tool=="Spray Paint" and cooltool!="Spec Spray":
                tool="None"
                cooltool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(spraycanpic,(688,194))
                screen.blit(spraypaintdes,(697,119))
                tool="Spray Paint"
        if mb[0]==1 and floodfillrect.collidepoint(mx,my) and omb != mb:
            if tool=="Bucket":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                tool="Bucket"
                cooltool="None"
                screen.blit(paintbucketpic,(688,194))
                screen.blit(paintbucketdes,(697,119))
        if mb[0]==1 and clearrect.collidepoint(mx,my) and omb != mb:
            screen.blit(clearpic,(688,194))
            screen.blit(cleardes,(697,119))
            draw.rect(screen,(255,255,255),(35,110,620,630))
        if mb[0]==1 and paintrect.collidepoint(mx,my) and omb != mb:
            if tool=="Brush":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(paintbrushpic,(688,194))
                screen.blit(paintdes,(697,119))
                tool="Brush"
                cooltool="None"
        if mb[0]==1 and eraserrect.collidepoint(mx,my) and omb != mb:
            if tool=="Eraser":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(eraserpic,(688,194))
                screen.blit(eraserdes,(697,119))
                tool="Eraser"
                cooltool="None"
        if mb[0]==1 and pencilrect.collidepoint(mx,my) and omb != mb:
            if tool=="Pencil":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(pencilpic,(688,194))
                screen.blit(pencildes,(697,119))
                tool="Pencil"
                cooltool="None"
        if mb[0]==1 and linerect.collidepoint(mx,my) and omb != mb:
            if tool=="Line":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(linepic,(688,194))
                screen.blit(linedes,(697,119))
                tool="Line"
                cooltool="None"
        if mb[0]==1 and colourselect.collidepoint(mx,my) and omb != mb:
            if tool=="ColourSelect":
                tool="None"
                screen.blit(wolftool,(688,194))
                screen.blit(please,(697,119))
            else:
                screen.blit(dropperpic,(688,194))
                screen.blit(dropperdes,(697,119))
                tool="ColourSelect"
                cooltool="None"
        if mb[0]==1 and specrect.collidepoint(mx,my):
            colour=screen.get_at((mx,my))    #change colour
        ###############SSPEC TOOL ADD ONN############
        if cooltool== "Spec Tool" and tool=="Spray Paint" or cooltool== "Spec Spray" and tool=="Spray Paint":
            cooltool="Spec Spray"
            screen.blit(specspraypic,(688,194))
            screen.blit(specspraydes,(697,119))
        #############################################
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            redolist=[]      #Resets the Redo list when something new is being done
            if tool=="Cool Rect":
                screen.blit(canvasback,(35,110))
                if size%2==0:   #we want the number to be odd becuase if it isnt then it draws the length
                    size=size-1 #of the line a littlee bit extra but its noticible
                    flag=True
                if mx<posA and my<posB:
                    left=posA+(size/2)  ##since mx,my will be in the middle of the lines thickness we have to divide by 2
                    top=posB+(size/2)
                    right=mx-(size/2)
                    bottom=my-(size/2)
                    draw.rect(screen,clrs[len(clrs)-1],(mx,my,posA-mx,posB-my))
                    draw.line(screen,clrs[len(clrs)-2],(left,posB),(right,posB),size)
                    draw.line(screen,clrs[len(clrs)-2],(posA,top),(posA,bottom),size)
                    draw.line(screen,clrs[len(clrs)-2],(left,my),(right,my),size)
                    draw.line(screen,clrs[len(clrs)-2],(mx,top),(mx,bottom),size)
                else:                
                    left=posA-(size/2) #the else is for the top left section on a cartesian plane
                    top=posB-(size/2)
                    right=mx+(size/2)
                    bottom=my+(size/2)
                    draw.rect(screen,clrs[len(clrs)-1],(posA,posB,mx-posA,my-posB))
                    draw.line(screen,clrs[len(clrs)-2],(left,posB),(right,posB),size)
                    draw.line(screen,clrs[len(clrs)-2],(posA,top),(posA,bottom),size)
                    draw.line(screen,clrs[len(clrs)-2],(left,my),(right,my),size)
                    draw.line(screen,clrs[len(clrs)-2],(mx,top),(mx,bottom),size)
                if flag==True: ##reset the value back to the original
                    size=size+1
                    flag=False
            if cooltool=="Spec Spray":
                specspray(mx,my,ol,colour)
            if cooltool=="Spec Tool":
                spec(mx,my,ol,colour)
            if tool=="ColourSelect":
                colour=screen.get_at((mx,my))
            if tool=="Bucket" and flag==True:
                screen.set_clip(None)
                oldclr=screen.get_at((mx,my))
                ffill(mx,my,colour,oldclr)
                points=[]
                screen.blit(paintbucketdes,(697,119))
                flag=False
                screen.set_clip(canvas)
            if tool=="Bucket" and flag==False and omb!=mb: ##the whole flag business here is so that the picture blits, runs the rest of the 
                screen.set_clip(None)                   ## loop and then does the bucket tool, otherwise the please wait picture will not blit before the 
                screen.blit(pleasewait,(697,119))         ##paint bucket function is called, unless it goes through the loop.
                flag=True
                screen.set_clip(canvas)
            if tool=="Triangle":
                screen.blit(canvasback,(35,110))
                draw.line(screen,colour,(posA,posB),(posA+(mx-posA),posB),size)
                draw.line(screen,colour,(posA,posB),(posA,posB+(my-posB)),size)
                draw.line(screen,colour,(posA,posB+(my-posB)),(posA+(mx-posA),posB),size)           
            if tool=="Filled Elipse":
                screen.blit(canvasback,(35,110)) 
                if abs(posA-mx) >1 and abs(posB-my) >1: ##so it doesnt crash saying the width is greater than radius
                    radx = abs(mx-posA)
                    rady = abs(my-posB)
                    if mx>posA and my > posB:     #4 if statements for the 4 qudrents on the cartetian plane
                            draw.ellipse(screen,colour,(posA,posB,radx,rady))
                    if mx<posA and my<posB:
                            draw.ellipse(screen,colour,(mx,my,radx,rady))
                    if mx>posA and my < posB:
                            draw.ellipse(screen,colour,(posA,my,radx,rady))
                    if mx<posA and my > posB:
                            draw.ellipse(screen,colour,(mx,posB,radx,rady))  
            if tool=="Empty Elipse":
                screen.blit(canvasback,(35,110))
                if abs(posA-mx) >1 and abs(posB-my) >1:
                    radx = abs(mx-posA)
                    rady = abs(my-posB)
                    if mx>posA and my > posB:
                            draw.ellipse(screen,colour,(posA,posB,radx,rady),1)
                    if mx<posA and my<posB:
                            draw.ellipse(screen,colour,(mx,my,radx,rady),1)
                    if mx>posA and my < posB:
                            draw.ellipse(screen,colour,(posA,my,radx,rady),1)
                    if mx<posA and my > posB:
                            draw.ellipse(screen,colour,(mx,posB,radx,rady),1)  
            if tool=="Empty Rectangle":
                screen.blit(canvasback,(35,110))
                if size%2==0:     ##explained in the filled rectange tool above
                    size=size-1
                    flag=True
                if mx<posA and my<posB:
                    left=posA+(size/2)
                    top=posB+(size/2)
                    right=mx-(size/2)
                    bottom=my-(size/2)
                    draw.line(screen,colour,(left,posB),(right,posB),size)
                    draw.line(screen,colour,(posA,top),(posA,bottom),size)
                    draw.line(screen,colour,(left,my),(right,my),size)
                    draw.line(screen,colour,(mx,top),(mx,bottom),size)
                else:                
                    left=posA-(size/2)
                    top=posB-(size/2)
                    right=mx+(size/2)
                    bottom=my+(size/2)
                    draw.line(screen,colour,(left,posB),(right,posB),size)
                    draw.line(screen,colour,(posA,top),(posA,bottom),size)
                    draw.line(screen,colour,(left,my),(right,my),size)
                    draw.line(screen,colour,(mx,top),(mx,bottom),size)
                if size%2==1 and flag==True:
                    size=size+1
                    flag=False
            if tool=="Rectangle Filled":       
                if mb[0]==1:
                    screen.blit(canvasback,(35,110))
                    draw.rect(screen,colour,(posA,posB,mx-posA,my-posB))
            if tool=="Spray Paint" and cooltool != "Spec Spray":
                mx,my=mouse.get_pos()
                for i in range(size*2):
                    rmx=randint(-1*(size+15),size+15)
                    rmy=randint(-1*(size+15),size+15)
                    dist=(((mx-(mx+rmx)))**2+(my-(my+rmy))**2)**0.5
                    if dist < size:
                        draw.line(screen,colour,(mx+rmx,my+rmy),(mx+rmx,my+rmy))
            if tool=="Brush":
                xdif=mx-omx
                ydif=my-omy
                dist=(xdif**2+ydif**2)**0.5
                if dist>0:
                    for i in range(int(dist)): ##using similar triangles it draws a circle at every integer starting at 0 until its one less than dist.
                        draw.circle(screen,colour,(omx+int(i*xdif/dist),omy+int(i*ydif/dist)),size)
                else:
                    draw.circle(screen,colour,(mx,my),size)
            if tool=="Eraser":
                xdif=mx-omx
                ydif=my-omy
                dist=(xdif**2+ydif**2)**0.5
                if dist>0:
                    for i in range(int(dist)):
                        draw.rect(screen,(255,255,255),(omx+int(i*xdif/dist)-size/2,(omy+int(i*ydif/dist))-size/2,size,size))
                else:
                    draw.rect(screen,(255,255,255),(mx-size/2,my-size/2,size,size))
            if tool=="Pencil":
                draw.line(screen,colour,(omx,omy),(mx,my))
            if tool=="Line":
                screen.blit(canvasback,(35,110))
                draw.line(screen, (colour), start,(mx,my), size)
            screen.set_clip(None)
########THIS IS THE END OF TOOLS#########
    display.flip()
font.quit()
del comicFont
quit()
