def moveForwards(Player, Game):
    if Player.location[0] >= 1800:
        Game.move(10)
        Player.move(0)
    elif Player.location[0] < 1800 and Player.location[0] < 1000:
        Game.move(0)
        Player.move(10)
    else:
        Game.move(6)
        Player.move(4)

def moveBackwards(Player, Game):
    Game.move(0)
    Player.move(-7)

def playerjump(Player, Game): # 15 starting and taking away 1 workds
    if Player.jumping == False:
        Player.jumping = True
        Player.jumpingVelocity = 15

    if Player.jumpingVelocity >= 0 and Player.jumping:
        Game.move(0)
        Player.jump()
        Player.jumpingVelocity -= 1

    if Player.jumpingVelocity < 0 and Player.jumping and Player.jumpingVelocity >= -15:
        Game.move(0)
        Player.jump()
        Player.jumpingVelocity -= 1

    if Player.jumpingVelocity == -16:
        Player.jumping = False



    # Going up

    # if Player.jumping == False:
    #     Player.jumping = True
    #     Player.jumpingVelocity = 10

    # if Player.jumping:
    #     Player.jump()
    #     Player.jumpingVelocity -= 1
    #     if Player.jumpingVelocity >= 10:
    #         Player.jumping = False




    # if Player.jumping == False:
    #     for i in range(0, 12):
    #         Game.move(0)
    #         Player.jump(True)
    #         pygame.display.flip()
    #         Player.jumping = True

    #     # Going back down
    #     if Player.jumping:
    #         for i in range(0, 12):
    #             Game.move(0)
    #             Player.jump()
    #             pygame.display.flip()
    #             Player.jumping = False