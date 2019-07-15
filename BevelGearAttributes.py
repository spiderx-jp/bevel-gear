import math

class BevelGearAttributes:

    def __init__(self, teeth, module, shaftAngle, faceWidth):
        self.teeth = teeth
        self.module = module
        self.shaftAngle = shaftAngle
        self.faceWidth = faceWidth

    @classmethod
    def createGearPair(cls, gearTeeth, pinionTeeth, module, shaftAngle, faceWidth):
        gear = cls(gearTeeth, module, shaftAngle, faceWidth)
        pinion = cls(gearTeeth, module, shaftAngle, faceWidth)

        referenceDiameterPinion = pinionTeeth * module
        referenceDiameterGear = gearTeeth * module
        
        referenceConeAnglePinion = math.atan(math.sin(math.radians(shaftAngle)) / (gearTeeth/pinionTeeth + math.cos(math.radians(shaftAngle))))
        referenceConeAngleGear = shaftAngle - math.degrees(referenceConeAnglePinion)

        coneDistance = referenceConeAngleGear / (2 * math.sin(math.radians(referenceConeAngleGear)))
        
        if (faceWidth > coneDistance / 3):
            print("Oh noes.")
        
        _temp = (gearTeeth * math.cos(math.radians(referenceConeAnglePinion)) / pinionTeeth * math.cos(math.radians(referenceConeAngleGear)))
        addendumGear = 0.54*module + 0.46*module / _temp
        addendumPinion = 2*module - addendumGear
        
        dedendumGear = 2.188 * module - addendumGear
        dedendumPinion = 2.188 * module - addendumPinion

        return (gear, pinion)
