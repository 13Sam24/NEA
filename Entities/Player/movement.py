def moveForwards(Player, Game):
    if Player.checkCollision(Game.chunklist) == False:
        if Player.location[0] >= 1800:
            Game.move(10)
            Player.move(0)
        elif Player.location[0] < 1000:
            Game.move(0)
            Player.move(10)
        else:
            Game.move(6)
            Player.move(4)
    else:
        print('collision')

        

def moveBackwards(Player, Game):
    Game.move(0)
    Player.move(-7)

def playerjump(Player, Game): # 15 starting and taking away 1 workds
    if Player.jumping == False:
        Player.jumping = True
        Player.jumpingVelocity = 15

    if Player.jumpingVelocity >= 0 and Player.jumping:
        if Player.checkCollision(Game.chunklist) == False:
            Game.move(0)
            Player.jump()
            Player.jumpingVelocity -= 1
        else:
            Player.jumpingVelocity == 0


    if Player.jumpingVelocity < 0 and Player.jumping and Player.jumpingVelocity >= -15:
        if Player.checkCollision(Game.chunklist) == False:
            Game.move(0)
            Player.jump()
            Player.jumpingVelocity -= 1
        else:
            Player.jumpingVelocity == -16
            
    if Player.jumpingVelocity == -16:
        Player.jumping = False