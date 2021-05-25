#! /usr/bin/python3

import random

class Uav:

    # posicionamento
    posX = 0
    posY = 0
    posZ = 0

    # velocidades
    velMin = 0
    velMax = 0
    vel=0

    # autonomia da bateria em M
    autonomia = 10000

    # construtor UAV
    def __init__(self, posX:float, posY:float, posZ:float,
                 velMin:float, velMax:float,autonomia:float):
        # posicionamento
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

        # velocidades
        self.velMin = velMin
        self.velMax = velMax
        self.vel = random.uniform(velMin,velMax)

        # autonomia da bateria em KM
        self.autonomia = autonomia

    # obter=======================
    def getPosX(self) -> float:
        return self.posX

    def getPosY(self) -> float:
        return self.posY

    def getPosZ(self) -> float:
        return self.posZ

    def getVel(self) -> float:
        return  self.vel

    def getAutonomia(self) -> float:
        return self.autonomia

    # atualizar================
    def setPosX(self,x) :
        self.posX = x

    def setPosY(self,y):
        self.posY = y

    def setPosZ(self,z):
        self.posZ = z

    def setAuonomia(self,autonomia):
        self.autonomia = autonomia


