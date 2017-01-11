class SuccessorState(object):

    def __init__(self,mR = 0, cR = 0, bR = 0, mL = 0, cL = 0, bL = 0):

        self.mRight = (mR)
        self.mLeft = (mL)
        self.cRight = (cR)
        self.cLeft = (cL)
        self.rBoat = (bR)
        self.lBoat = (bL)
        self.myMax = 0
        self.key = ""
        self.depth = 0
        self.successorStates = []
        self.parentNode = []
        self.heuristicValue = 10

    def __lt__(self, other):
        selfPriority = (self.heuristicValue)
        otherPriority = (other.heuristicValue)
        if selfPriority < otherPriority:
            return True
        else:
            return False

    def showState(self):
        print "--------------"
        print"--M:" + str(self.mLeft) + "--C:" + str(self.cLeft) + "--B:" + str(self.lBoat)
        print"--M:" + str(self.mRight) + "--C:" + str(self.cRight) + "--B:" + str(self.rBoat)


    def expandState(self):
        #Perform one of the 5 operations, in order...
        myStates = []
        for x in range(0,5):
            newState = SuccessorState()
            newState.myMax = self.myMax
            myStates.append(newState)
            if x == 0:
                #Lets move 1 Missionary
                if self.rBoat == 1:
                    myStates[0].mRight = self.mRight - 1
                    myStates[0].mLeft = self.mLeft +1
                    myStates[0].cLeft = self.cLeft
                    myStates[0].cRight = self.cRight

                    myStates[0].rBoat = 0
                    myStates[0].lBoat = 1
                    myStates[0].key = str(myStates[0].mRight)+str(myStates[0].cRight)+str(myStates[0].rBoat)+str(myStates[0].mLeft)+str(myStates[0].cLeft)+str(myStates[0].lBoat)
                    myStates[0].depth = self.depth + 1
                elif self.lBoat == 1:
                    myStates[0].mLeft = self.mLeft - 1
                    myStates[0].mRight = self.mRight + 1
                    
                    myStates[0].cLeft = self.cLeft
                    myStates[0].cRight = self.cRight

                    myStates[0].rBoat = 1
                    myStates[0].lBoat = 0
                    myStates[0].key = str(myStates[0].mRight)+str(myStates[0].cRight)+str(myStates[0].rBoat)+str(myStates[0].mLeft)+str(myStates[0].cLeft)+str(myStates[0].lBoat)
                    myStates[0].depth = self.depth + 1


            elif x == 1:
                #Lets move two missionaries
                if self.rBoat == 1:
                    myStates[1].mRight = self.mRight-2
                    myStates[1].mLeft =  self.mLeft+2
                    myStates[1].cLeft = self.cLeft
                    myStates[1].cRight = self.cRight                    
                    myStates[1].rBoat = 0
                    myStates[1].lBoat = 1
                    myStates[1].key = str(myStates[1].mRight)+str(myStates[1].cRight)+str(myStates[1].rBoat)+str(myStates[1].mLeft)+str(myStates[1].cLeft)+str(myStates[1].lBoat)
                    myStates[1].depth = self.depth + 1


                elif self.lBoat == 1:
                    myStates[1].mLeft = self.mLeft - 2
                    myStates[1].mRight = self.mRight + 2
                    myStates[1].cLeft = self.cLeft
                    myStates[1].cRight = self.cRight                    
                    myStates[1].rBoat = 1
                    myStates[1].lBoat = 0
                    myStates[1].key = str(myStates[1].mRight)+str(myStates[1].cRight)+str(myStates[1].rBoat)+str(myStates[1].mLeft)+str(myStates[1].cLeft)+str(myStates[1].lBoat)
                    myStates[1].depth = self.depth + 1


            elif x == 2:
                #Let's move one cannibal
                if self.rBoat == 1:
                    myStates[2].cRight = self.cRight -1
                    myStates[2].cLeft = self.cLeft +1
                    myStates[2].mLeft = self.mLeft
                    myStates[2].mRight = self.mRight                      
                    myStates[2].rBoat = 0
                    myStates[2].lBoat = 1
                    myStates[2].key = str(myStates[2].mRight)+str(myStates[2].cRight)+str(myStates[2].rBoat)+str(myStates[2].mLeft)+str(myStates[2].cLeft)+str(myStates[2].lBoat)
                    myStates[2].depth = self.depth + 1


                elif self.lBoat == 1:
                    myStates[2].cLeft =  self.cLeft - 1
                    myStates[2].cRight =  self.cRight + 1
                    myStates[2].mLeft = self.mLeft
                    myStates[2].mRight = self.mRight  
                    myStates[2].rBoat = 1
                    myStates[2].lBoat = 0
                    myStates[2].key = str(myStates[2].mRight)+str(myStates[2].cRight)+str(myStates[2].rBoat)+str(myStates[2].mLeft)+str(myStates[2].cLeft)+str(myStates[2].lBoat)
                    myStates[2].depth = self.depth + 1


            elif x == 4:

                #Let's move two cannibals
                if self.rBoat == 1:
                    myStates[4].cRight =  self.cRight - 2
                    myStates[4].cLeft = self.cLeft + 2
                    myStates[4].mLeft = self.mLeft
                    myStates[4].mRight = self.mRight  
                    myStates[4].rBoat = 0
                    myStates[4].lBoat = 1
                    myStates[4].key = str(myStates[4].mRight)+str(myStates[4].cRight)+str(myStates[4].rBoat)+str(myStates[4].mLeft)+str(myStates[4].cLeft)+str(myStates[4].lBoat)
                    myStates[4].depth = self.depth + 1


                elif self.lBoat == 1:
                    myStates[4].cLeft = self.cLeft - 2
                    myStates[4].cRight = self.cRight + 2
                    myStates[4].mLeft = self.mLeft
                    myStates[4].mRight = self.mRight  
                    myStates[4].rBoat = 1
                    myStates[4].lBoat = 0
                    myStates[4].key = str(myStates[4].mRight)+str(myStates[4].cRight)+str(myStates[4].rBoat)+str(myStates[4].mLeft)+str(myStates[4].cLeft)+str(myStates[4].lBoat)
                    myStates[4].depth = self.depth + 1

            elif x == 3:
                #Let's move a cannibal and missionary
                if self.rBoat == 1:
                    myStates[3].mRight = self.mRight - 1
                    myStates[3].cRight =  self.cRight - 1
                    myStates[3].mLeft = self.mLeft + 1
                    myStates[3].cLeft = self.cLeft + 1
                    myStates[3].rBoat = 0
                    myStates[3].lBoat = 1
                    myStates[3].key = str(myStates[3].mRight)+str(myStates[3].cRight)+str(myStates[3].rBoat)+str(myStates[3].mLeft)+str(myStates[3].cLeft)+str(myStates[3].lBoat)
                    myStates[3].depth = self.depth + 1


                elif self.lBoat == 1:
                    myStates[3].mRight =  self.mRight + 1
                    myStates[3].cRight = self.cRight + 1
                    myStates[3].mLeft = self.mLeft - 1
                    myStates[3].cLeft = self.cLeft - 1   
                    myStates[3].rBoat = 1
                    myStates[3].lBoat = 0
                    myStates[3].key = str(myStates[3].mRight)+str(myStates[3].cRight)+str(myStates[3].rBoat)+str(myStates[3].mLeft)+str(myStates[3].cLeft)+str(myStates[3].lBoat)
                    myStates[3].depth = self.depth + 1

        validStates = []
        for x in myStates:
            if x.isValid():
                x.parentNode.append(self)
                self.successorStates.append(x) 
            
       
    def isValid(self):
    	if (self.mRight > self.myMax) or (self.mRight < 0):
    		return False
    	if (self.cRight > self.myMax) or (self.cRight < 0):
    		return False
    	if (self.mLeft > self.myMax) or (self.mLeft < 0):
    		return False
    	if (self.cLeft > self.myMax) or (self.cLeft < 0):
    		return False    	

        if (self.mRight < self.cRight):
        	if (self.mRight > 0):
        		return False

        if (self.mLeft < self.cLeft):
            if self.mLeft > 0:
        	   return False
            else:
                pass

        return True

    def isIdentical(self,potential):
        myBool = True
        if self.mRight != potential.mRight:
            myBool = False
        if self.mLeft != potential.mLeft:
            myBool = False
        if self.cLeft != potential.cLeft:
            myBool = False                        
        if self.cRight != potential.cRight:
            myBool = False
        if self.rBoat != potential.rBoat:
            myBool = False
        if self.lBoat != potential.lBoat:
            return False
        return myBool    
    def getHeuristic(self,init):
        if init.rBoat == 1:
            self.heuristicValue = init.mRight - self.mLeft
        elif init.lBoat == 1:
            self.heuristicValue = init.mLeft - self.mRight 


    def checkForGoal(self, goal_state):
        if(self.mRight == goal_state.mRight):
            if self.cRight == goal_state.cRight:
                if self.mLeft == goal_state.mLeft:
                    if self.cLeft == goal_state.cLeft:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
