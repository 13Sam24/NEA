def moveForwards(Player, Game):
    if Player.checkCollision(Game.chunklist, 2, 0) == False:
        if Player.location[0] >= 1600:
            Game.move(2)
            Player.move(0)
        else:
            Game.move(0)
            Player.move(2)

        

def moveBackwards(Player, Game):
    if Player.checkCollision(Game.chunklist, -1, 0) == False:
        Game.move(0)
        Player.move(-1)


def playerjump(Player, Game): # 15 starting and taking away 1 workds
    if Player.jumping == False:
        Player.jumping = True
        Player.jumpingVelocity = 16 # 15 works

    # Going up
    if Player.jumpingVelocity >= 0 and Player.jumping:
        if Player.checkCollision(Game.chunklist, 0, Player.jumpingVelocity) == False:
            Game.move(0)
            Player.jump()
            Player.jumpingVelocity -= 1
        else:
            Player.jumpingVelocity == 0

    # Comming back down
    if Player.jumpingVelocity < 0 and Player.jumping and Player.jumpingVelocity >= -15:
            if Player.checkCollision(Game.chunklist, 0, Player.jumpingVelocity) == False:
                Game.move(0)
                Player.jump()
                Player.jumpingVelocity -= 1
            else:
                Player.jumpingVelocity = -16
            
    if Player.jumpingVelocity == -16:
        Player.jumping = False

def playerfall(Player, Game):
    if Player.checkCollision(Game.chunklist, 0, -1) == False:
        Game.move(0)
        Player.fall()