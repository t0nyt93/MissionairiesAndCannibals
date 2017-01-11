import sys
import os
from myStates import SuccessorState as ss
import Queue as q
import time

NODE_EXPANSIONS = 0

def getStartingStates(initial_file,goal_file,initial_state,goal_state):
	with open(initial_file, 'r+') as infile:
		leftBank = infile.readline()
		rightBank = infile.readline()

		leftBank = leftBank.replace(" ", ",").strip('\n').split(',')
		rightBank = rightBank.replace(" ", ",").strip('\n').split(',')

		initial_state.mRight = int(rightBank[0]) 
		initial_state.mLeft = int(leftBank[0])
		
		initial_state.cRight = int(rightBank[1])
		initial_state.cLeft = int(leftBank[1])

		initial_state.lBoat = int(leftBank[2])
		initial_state.rBoat = int(rightBank[2])

		infile.close()
	
	with open(goal_file, 'r+') as infile:
		goalLeftBank = infile.readline()
		goalRightBank = infile.readline()
		goalLeftBank = goalLeftBank.replace(" ", ",").strip('\n').split(',')
		goalRightBank = goalRightBank.replace(" ", ",").strip('\n').split(',')

		goal_state.mRight = int(goalRightBank[0] )
		goal_state.mLeft = int(goalLeftBank[0])
		
		goal_state.cRight = int(goalRightBank [1] )
		goal_state.cLeft = int(goalLeftBank[1])

		goal_state.lBoat = int(goalLeftBank[2])
		goal_state.rBoat = int(goalRightBank[2])
		
		infile.close()
	if int(goal_state.mRight) != 0:
		initial_state.myMax = int(goal_state.mRight)
	if int(goal_state.mLeft) != 0:
		initial_state.myMax = int(goal_state.mLeft)
	initial_state.key = str(initial_state.mRight)+str(initial_state.cRight)+str(initial_state.rBoat)+str(initial_state.mLeft)+str(initial_state.cLeft)+str(initial_state.lBoat)
	initial_state.depth = 0
	goal_state.depth = 0


def BreadthFirst(initial_state, goal_state, outputFile):
	print ("This is BreadthFirst")
	myQueue = q.Queue()
	visited = []
	V = {}
	#Put starting node on queue
	myQueue.put(initial_state)
	currState = ss()
	counter = 0
	try:
		while not myQueue.empty(): #If fringe is empty, return failure
			currState = myQueue.get() #Remove-Front(Fringe)
			currState.myMax = initial_state.myMax #Some programming bogus
			if(currState.isIdentical(goal_state)): #If Goal Test -------
				print ("Solution Found!")
				break
			else:
				counter = counter + 1			# If not Goal Test add as a node visited
			#If we've already seen this configuration, don't include the node. 
			if currState.key in V:	
				pass
			#Otherwise if it's new let's expand it 
			else:
				currState.expandState()
				#Add it to the list of nodes visited
				V[currState.key] = currState
				#for all successor states that are valid
				for x in currState.successorStates:
					#If we've already seen it, AKA reverted back to an old stage,
					if x.key in V:
						#remove that state
						currState.successorStates.remove(x)
			#Place all qualifying succesors back onto the queue. 		
			for item in currState.successorStates:
				myQueue.put(item)
		if myQueue.empty():
			print "Unable to find a solution. Ran out of states to check."

	except KeyboardInterrupt:
		pass
	print ("We opened " + str(counter) + " nodes!")
	savePath(currState,initial_state,outputFile)
	return counter

def DepthFirst(initial_state, goal_state, outputFile):
	print ("This is DepthFirst")
	myQueue = list()
	visited = []
	V = {}
	#NODE_EXPANSIONS += len(initial_state.successorStates)
	#Put starting node on queue
	myQueue.append(initial_state)

	currState = ss()
	counter = 0
	try:
		while len(myQueue) != 0: #If fringe is empty, return failure
			currState = myQueue.pop() #Remove-Front(Fringe)
			currState.myMax = initial_state.myMax #Some programming bogus
			if(currState.isIdentical(goal_state)): #If Goal Test -------
				print ("Solution Found!")
				break
			else:
				counter += 1						# -----------------------
			#Create list of valid successorState
			if currState.key in V:
				pass
			else:
				currState.expandState()
				V[currState.key] = currState
				for x in currState.successorStates:
					if x.key in V:
						currState.successorStates.remove(x)
					
			for item in currState.successorStates:
				myQueue.append(item)
		if len(myQueue) == 0:
			print "Unable to find a solution. Ran out of states to check."

	except KeyboardInterrupt:
		pass
	print ("We opened " + str(counter) + " nodes!")
	savePath(currState,initial_state,outputFile)
	return counter

def IterativeDeep(initial_state, goal_state, outputFile):
	print ("Iterative Deepening" )
	myQueue = list()
	visited = []
	V = {}
	#NODE_EXPANSIONS += len(initial_state.successorStates)
	#Put starting node on queue
	myQueue.append(initial_state)
	myCurrentTraverse = list()
	currState = ss()
	counter = 0
	maxDepth = 1
	try:
		while True: #If fringe is empty, return failure
			if len(myQueue) > 0:
				currState = myQueue.pop() #Remove-Front(Fringe)
			else:
				print ("No more items. Failure to find solution")
				break
			if currState.depth > maxDepth:
				myQueue.insert(0,currState)
			else:
				#Lets traverse this node to the max depth.
				myCurrentTraverse.append(currState)
				while currState.depth <= maxDepth:
					if len(myCurrentTraverse) > 0:
						currState = myCurrentTraverse.pop()
					else:
						break
					currState.myMax = initial_state.myMax #Some programming bogus

					if currState.key in V:
						pass
					else:
						if(currState.isIdentical(goal_state)): #If Goal Test -------
							break
						else:
							counter += 1
							currState.expandState()
							V[currState.key] = currState
					for x in currState.successorStates:
						if x.key in V:
							currState.successorStates.remove(x)
					
					for item in currState.successorStates:
						myQueue.append(item)
						myCurrentTraverse.append(item)
				if(currState.isIdentical(goal_state)): #If Goal Test -------
					print ("Solution Found!")
					break
				maxDepth += 1

	except KeyboardInterrupt:
		pass
	print ("We opened " + str(counter) + " nodes!")
	savePath(currState,initial_state,outputFile)
	return counter

def aStarSearch(initial_state, goal_state,outputFile):
	print ("A* Search"	)
	myQueue = q.PriorityQueue()
	visited = []
	V = {}
	#NODE_EXPANSIONS += len(initial_state.successorStates)
	#Put starting node on queue
	initial_state.getHeuristic(initial_state)
	myQueue.put(initial_state)
	#currState = ss()
	counter = 0
	try:
		while not myQueue.empty(): #If fringe is empty, return failure
			currState = myQueue.get() #Remove-Front(Fringe)
			currState.getHeuristic(initial_state)
			currState.myMax = initial_state.myMax #Some programming bogus
	
			if(currState.isIdentical(goal_state)): #If Goal Test -------
				print ("Solution Found!")
				break
			else:
				#IT wasn't a goal node, so it's one we will VISIT and expand possibly
				counter += 1
			#Create list of valid successorState
			
			if currState.key in V:
				pass
			else:
				currState.expandState()
				V[currState.key] = currState
				for x in currState.successorStates:
					if x.key in V:
						currState.successorStates.remove(x)
					
			for item in currState.successorStates:
				item.getHeuristic(initial_state)
				myQueue.put(item)
		if myQueue.empty():
			print "Unable to find a solution. Ran out of states to check."
	except KeyboardInterrupt:
		pass
	print ("We opened " + str(counter) + " nodes!")
	savePath(currState,initial_state,outputFile)
	return counter

def savePath(myState,initial_state,outputFile):
	#This is what we're going to print to a file...
	with open(outputFile, 'w') as outfile:
		ourDepth = 0
		firstMove = 0
		while not myState.isIdentical(initial_state):
			if firstMove == 0:
				ourDepth = myState.depth
				outfile.write("Solution found at a depth of -" + str(myState.depth) + "-\n")
				outfile.write("--Mr:" +str(myState.mRight) + " --Cr:" +str(myState.cRight) + " --Br:" +str(myState.rBoat) + "\n" +  "--Ml:" +str(myState.mLeft) + " --Cl:" +str(myState.cLeft) + " --Bl:" + str(myState.lBoat) + '\n') 
				firstMove += 1
				outfile.write("Break\n")
				myState.showState()
			myState = myState.parentNode[0]
			outfile.write("--Mr:" +str(myState.mRight) + " --Cr:" +str(myState.cRight) + " --Br:" +str(myState.rBoat) + "\n" +  "--Ml:" +str(myState.mLeft) + " --Cl:" +str(myState.cLeft) + " --Bl:" + str(myState.lBoat) + '\n') 
			outfile.write("Break\n")
			myState.showState()
		print "Solution found at a depth of " + str(ourDepth)
def main():
	#Name of the script
	print ("Running " + sys.argv[0])
	if len(sys.argv) < 5:
		print ("Invalid command line arguments")
		sys.exit()

	#Read in the name of our initial and goal state files
	initFileName = sys.argv[1]
	goalFileName = sys.argv[2]

	#Get our starting states
	initState = ss()
	goalState = ss()

	#initialize the start
	getStartingStates(initFileName,goalFileName,initState,goalState)

	#Lets see if it worked...
	initState.parentNode.append(initState)
	#Figure out what method we're using
	ourSearch = sys.argv[3]
	outputFile = sys.argv[4]

	if ourSearch == "bfs":
		ourNodes = BreadthFirst(initState,goalState,outputFile)
		print "Nodes expanded:" + str(ourNodes)

	elif ourSearch == "dfs":
		ourNodes = DepthFirst(initState,goalState,outputFile)
		print "Nodes expanded:" + str(ourNodes)


	elif ourSearch == "iddfs":
		ourNodes = IterativeDeep(initState,goalState,outputFile)
		print "Nodes expanded:" + str(ourNodes)


	elif ourSearch == "astar":
		ourNodes = aStarSearch(initState,goalState,outputFile)
		print "Nodes expanded:" + str(ourNodes)
		

	else:
		print ("Sorry that wasn't a valid mode!")

	print ("This is my main function")

if __name__ == '__main__':
	main()