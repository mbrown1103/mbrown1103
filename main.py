#Matt Brown
#Final Proj
#5001 
#create game with pygame

"""https://drive.google.com/file/d/1cn_ZK-5keRy82ngjMDB4Lz9apS70fgWK/view?usp=sharing"""

"""Game is based off an episode of a popular netflix show Squid Game where the player must cross a bridge and decide
between the left or right tile. It could either hold their weight or they plummet to the ground to their death.
The contestent must remember which tile the player in front of them stepped on that was safe"""

"""General notes:
- Left arrow picks left tile
- Right arrow picks right tile
- DO NOT SPAM THE KEYS OR HOLD DOWN THE ARROW KEYS!!!!!!! 
- keyboard can be sticky so sometimes you might hit the arrow once but it will bug out and move twice in a row. 
This only happens occasionally however.
"""

"""import pygame module and random"""
import pygame as py
import random as r

class Game():
    """Game class in which this whole game is based off"""

    def __init__(self,width=1200,height=750):
        """init global WIN for the window. Width and Height for the window params.
        all tile images initialized as well"""
        global WIN
        py.font.init()
        self.Font = py.font.SysFont("comisans",30)
        WIN = py.display.set_mode((width,height))
        FL = py.image.load('glass.png')
        FR = py.image.load('glass.png')
        SL = py.image.load('glass.png')
        SR = py.image.load('glass.png')
        TL = py.image.load('glass.png')
        TR = py.image.load('glass.png')
        FL = py.image.load('glass.png')
        FR = py.image.load('glass.png')
        FIFL = py.image.load('glass.png')
        FIFR = py.image.load('glass.png')
        SIXL = py.image.load('glass.png')
        SIXR = py.image.load('glass.png')

        """init tile x y locations and bridge trapdoors"""
        self.tilelocXL = []
        self.tilelocYL = []
        self.tilelocXR = []
        self.tilelocYR = []

        """linked list array that stores the locations of the weak and strong glass from randomtrapdoor gen method"""
        self.bridgeL = []
        self.bridgeR = []
      
        """initialize players and import game info"""
        self.players = [5,4,3,2,1]
        self.tile = 0
        self.broke = False
        self.dead = 0 
        self.alive = len(self.players) 

        """tile row list array"""
        self.row1 = [FL,SL,TL,FL,FIFL,SIXR]
        self.row2 = [FR,SR,TR,FR,FIFR,SIXR]
    
    def drawbridge(self):
        """draws bridge"""
        end = py.draw.rect(WIN,(255,0,0),(0,250,100,350))
        beg = py.draw.rect(WIN,(255,0,0),(1100,250,200,350))
        beamL = py.draw.rect(WIN,(255,0,0),(0,250,1200,10))
        beamR = py.draw.rect(WIN,(255,0,0),(0,600,1200,10))
        beam2L = py.draw.rect(WIN,(255,0,0),(0,375,1200,10))
        beam2R = py.draw.rect(WIN,(255,0,0),(0,475,1200,10))

    def initBridgeDict(self):
        """linked lists to create the bridge tempered glass traps. Left represents top tiles. Right represents bottom"""
        for L in range(6):
            ran = r.randint(0,1)
            self.bridgeL.append(ran)
            for R in range(1):
                """make sure only one of the glass tiles can have a 1"""
                if self.bridgeL[L]==1:
                    self.bridgeR.append(0)
                elif self.bridgeL[L]==0:
                    self.bridgeR.append(1)
        print(self.bridgeL,"\n",self.bridgeR)
        # return bridgeL,bridgeR

    def drawObj(self):
        """draw tiles and text"""
        n= 0
        m =0

        """creating tile vars for collecting tile data"""
        tilex1L = 0
        tiley1L = 0
        tilex2R = 0
        tiley2R = 0
        for i in range(len(self.row1)):
            """draws first row of glass tile"""
            """appends location of Left side tiles as tuples for later use"""
            n+=150
            tilexL = -50+n
            tileyL = 235
            WIN.blit(self.row1[i],(tilexL,tileyL))
            self.tilelocXL.append(tilexL)
            self.tilelocYL.append(tileyL)
        for x in range(len(self.row2)):
            """draws second row of glass tiles"""
            """appends location of Right side tiles as tuples for later use"""
            m += 150
            tilexR = -50 + m
            tileyR = 450
            WIN.blit(self.row2[x],(tilexR,tileyR))
            self.tilelocXR.append(tilexR)
            self.tilelocYR.append(tileyR)
        
        """keeps track of contestents alive and dead"""
        alive = self.Font.render("Remaining alive:" + str(self.alive),False,(0,255,255))
        dead = self.Font.render("Dead: " + str(self.dead),False,(255,0,0))
        squi = py.image.load('squid.png')
        tiletext = self.Font.render("Tile number: " + str(self.tile),False,(0,255,0))

        """create initial text"""
        WIN.blit(tiletext,(550,650))
        WIN.blit(squi,(100,0))
        WIN.blit(alive,(50,650))
        WIN.blit(dead,(1000,650))
    
    def controls(self,count):
        """Left and Right key control. Left and Right have implications for death,alive, and tile count vars"""
        keys = py.key.get_pressed()

        if (count == 6) and (keys[py.K_LEFT] or keys[py.K_RIGHT]):
            """if you are on the last tile before end platform it will add one to the tile list so
            the game win conditional can be met"""
            self.tile+=1
        else:
            if keys[py.K_LEFT] and (self.bridgeL[self.tile] == 0):
                """Player chooses left tile, but falls threw the weak glass"""   
                self.Left = True
                self.Right = False
                py.draw.rect(WIN,(0,0,0),(self.tilelocXL[self.tile]+50,315,150,40))
                self.tile+=1
                self.dead += 1
                self.alive -= 1
                self.players.pop()
                self.broke = True

            elif keys[py.K_LEFT] and (self.bridgeL[self.tile] == 1):
                """Player chooses left tile, and the glass supports his weight"""
                self.tile+=1
                self.broke = False

            if keys[py.K_RIGHT] and (self.bridgeR[self.tile] == 0):
                """Player chooses right tile, but falls threw the weak glass"""
                self.broke += 1
                py.draw.rect(WIN,(0,0,0),(self.tilelocXR[self.tile]+50,510,150,40))
                self.Right = True
                self.Left = False
                self.tile +=1
                self.dead += 1
                self.alive -= 1
                self.broke = True
                self.players.pop()

            elif keys[py.K_RIGHT] and (self.bridgeR[self.tile] == 1):
                """Player chooses right tile, and the glass supports his weight"""
                self.tile+=1
                self.broke = False

    def cursor(self,tile):
        """draws tile cursor. uses Count object from Game class for tile"""
        movevar = 150 *tile
        erasevar = 255 + movevar
        py.draw.rect(WIN,(0,0,0),(0,210,1200,30))
        py.draw.polygon(WIN,(0,255,0),((75+movevar,235),(65+movevar,210),(90+movevar,210)))

    def Win(self,count):
        """takes in count object to determine if win"""
        if count==7:
            return True
    
    def Lose(self,alive):
        """takes in alive param for alive count number"""
        if self.alive == 0:
            return True

    def isDead(self):
        """return whether the player has died or not"""
        if self.broke == True:
            return True

    def returnCount(self):
        """return tilecount"""
        return self.tile

    def returnDead(self):
        """return dead count"""
        return self.dead
    
    def returnAlive(self):
        """return Alive count"""
        return self.alive

    def resetPlayer(self,count,dead):
        """reset tiles uses dead param for isDead method object in main"""
        count = 0
        self.tile = count

    def Quit(self):
        keys = py.key.get_pressed()
        if keys[py.K_q]:
            py.quit
    
    def deletePLayers(self,number,players):
        """use recursion to delete preset number of players and add new ones. 
        Player param must be list. This is for people who want more than 5 players"""
        if number==0:
            players = self.players
            return players
        else:
            if len(self.players)>0:
                self.players.pop()
                return self.CreatePLayers(number-1,players)

    def addPlayers(self,number,players):
        """recursive function. Adds players from list to self.players"""
        if number == len(self.players):
            return self.players
        else:
            index = number-1
            self.players.append(players[index])
            return self.players[index-1]


def main():
    """mainstuff"""
    use = Game()
    tilecount = 0
    Font = py.font.SysFont("comisans",30)
    GameOver = py.image.load('squidcard.png')
    Piggy = py.image.load('win.png')

    """draw basis"""
    use.initBridgeDict()
    use.drawbridge()
    use.drawObj()
    
    """while loop for game"""
    
    running  = True
    while running == True:
        py.time.delay(100)
        for event in py.event.get(): 
            if event.type == py.QUIT:
                running = False
        
        """objects from class for counting"""
        Count = use.returnCount()
        Dead = use.returnDead()
        Alive = use.returnAlive()
        isDed = use.isDead()
        Lose__ = use.Lose(Alive)
        done = use.Win(Count)

        """game conditionals for basic menu and game operations"""
        if Count > 0:
            """update count on all text updates"""
            WIN.fill((0,0,0),(0,630,1200,500))
            tiletext = Font.render("Tile number: " + str(Count),1,(0,255,0))
            alive = Font.render("Remaining alive:" + str(Alive),1,(0,255,255))
            dead = Font.render("Dead: " + str(Dead),1,(255,0,0))
            WIN.blit(tiletext,(550,650))
            WIN.blit(alive,(50,650))
            WIN.blit(dead,(1000,650))

        """win lose conditionals"""
        if isDed == True and Count>0:
            """resets tile count back to zero when count is not at start and broke is True"""
            use.resetPlayer(0,isDed)
        if Lose__ == True:
            """Lose and quit"""
            WIN.blit(tiletext,(550,650))
            
            use.drawbridge()
            use.drawObj()
            WIN.blit(GameOver,(200,200))
            # running = False
        if done == True:
            """win and quit"""
            WIN.blit(Piggy,(400,175))
            # running = False
        if done == True or Lose__ == True:
            """if won or lost ensures players can continue to play do nothing"""
            
        else:
            """alow to use controls"""
            use.controls(Count)
            use.cursor(Count)

        py.display.update()
    
    py.quit()
        
if __name__ == "__main__":
    main()