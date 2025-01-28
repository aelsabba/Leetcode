######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################

# If you see different scores locally and on Gradescope this may be an
# indication that you are uploading a different file than the one you are
# executing locally. If this local ID doesn't match the ID on Gradescope then
# you uploaded a different file.
from rait import matrix
from copy import deepcopy
import math
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib
    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')

class Asteroid():
    def __init__(self,x_bounds,y_bounds, xy_start):
        self.n = 6
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        pUncertLocX = self.x_bounds
        pUncertLocY =self.y_bounds
        pUncertSpeedX = self.x_bounds  / 50
        pUncertSpeedY = self.y_bounds  / 50
        pUncertAccX = self.x_bounds  / 200
        pUncertAccY = self.y_bounds  / 200
        self.x = matrix([[xy_start[0]], ## xpos
                  [xy_start[1]],        ## ypos
                  [0],                  ## x velocity
                  [0],                  ## y velocity
                  [0],                  ## x acceleration
                  [0]])                 ## y accelration
        self.P = matrix([[pUncertLocX,0,0,0,0,0],
                        [0,pUncertLocY,0,0,0,0],
                        [0,0,pUncertSpeedX,0,0,0],
                        [0,0,0,pUncertSpeedY,0,0],
                        [0,0,0,0,pUncertAccX,0],
                         [0,0,0,0,0,pUncertAccY]])
        self.F = matrix([[1,0,1,0,0.5,0],
                         [0,1,0,1,0,0.5],
                         [0,0,1,0,1,0],
                         [0,0,0,1,0,1],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1]])
        self.H = matrix([[1,0,0,0,0,0],
                         [0,1,0,0,0,0]])
        self.R = matrix([[0.045 * 0.045,0],
                         [0,0.075 * 0.075]])

            #matrix([[0.045 * 0.045,0],
            #             [0,0.075 * 0.075]]))
        self.I = matrix([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1]])


    def update(self,z):
        ## start copy from lecture
        z = matrix([[z[0]],
                    [z[1]]])
        x_old = deepcopy(self.x)
        p_old = deepcopy(self.P)
        x_predicted = self.F * x_old
        p_predicted = self.F * p_old * self.F.transpose()
        y = z - self.H * x_predicted
        S = self.H * p_predicted * self.H.transpose() +  self.R
        K = p_predicted * self.H.transpose() * S.inverse()
        self.x = x_predicted + K * y
        self.P = (self.I - K * self.H) * p_predicted
        x_new = self.F * self.x
        return (x_new[0][0],x_new[1][0])
        ## end copy from lecture

class Spaceship():
    """The Spaceship to guide across the galaxy."""

    def __init__(self, bounds, xy_start):
        """Initialize the Spaceship."""
        self.x_bounds = bounds['x']
        self.y_bounds = bounds['y']
        self.agent_pos_start = xy_start
        self.asteroids = {}
        self.shipX = xy_start[0]
        self.shipY = xy_start[1]
        self.win = False



    def predict_from_observations(self, asteroid_observations):
        """Observe asteroid locations and predict their positions at time t+1.
        Parameters
        ----------
        self = a reference to the current object, the Spaceship
        asteroid_observations = A dictionary in which the keys represent asteroid IDs
        and the values are a dictionary of noisy x-coordinate observations,
        and noisy y-coordinate observations taken at time t.
        asteroid_observations format:
        ```
        `{1: (x-measurement, y-measurement),
          2: (x-measurement, y-measurement)...
          100: (x-measurement, y-measurement),
          }`
        ```

        Returns
        -------
        The output of the `predict_from_observations` function should be a dictionary of tuples
        of estimated asteroid locations one timestep into the future
        (i.e. the inputs are for measurements taken at time t, and you return where the asteroids will be at time t+1).

        A dictionary of tuples containing i: (x, y), where i, x, and y are:
        i = the asteroid's ID
        x = the estimated x-coordinate of asteroid i's position for time t+1
        y = the estimated y-coordinate of asteroid i's position for time t+1
        Return format:
        `{1: (x-coordinate, y-coordinate),
          2: (x-coordinate, y-coordinate)...
          100: (x-coordinate, y-coordinate)
          }`
        """
        asteroid_observations_rtrn = {}
        for key in asteroid_observations.keys():
            if key not in self.asteroids.keys():
                self.asteroids[key] = Asteroid(self.x_bounds[1],self.y_bounds[1],
                                               (0,0))
            asteroid = self.asteroids[key]
            asteroid_observations_rtrn[key] = asteroid.update(asteroid_observations[key])
            self.asteroids[key] = asteroid
        # tested_asteroid = 1
        # if tested_asteroid in asteroid_observations.keys():
        #    print( "x: %.3f -- x_meas: %.3f -- y: %.3f -- y_meas: %.3f" % (
        #     self.asteroids[tested_asteroid].x[0][0], asteroid_observations[tested_asteroid][0],
        #     self.asteroids[tested_asteroid].x[1][0], asteroid_observations[tested_asteroid][1]))


        # To view the visualization with the default pdf output (incorrect) uncomment the line below
        return asteroid_observations_rtrn

        # FOR STUDENT TODO: Update the Spaceship's estimate of where the asteroids will be located in the next time step
    def isWithinVerticalBounds(self,key):
        yMid = (self.y_bounds[0] + self.y_bounds[1])  / 2
        yWidth = abs(self.y_bounds[0] - self.y_bounds[1])
        yMin = yMid - 0.9 * (yWidth / 2.0)
        yMax = yMid + 0.9 * (yWidth / 2.0)
        if self.get_agent_pos(key)[1] > yMin:
            if self.get_agent_pos(key)[1] < yMax:
                return True
        else:
            return False

    def isWithinHorizontalBounds(self,key):
        xCenter = (self.x_bounds[0] + self.x_bounds[1])  / 2
        xWidth = abs(self.x_bounds[0] - self.x_bounds[1])
        xMin = xCenter - 0.8 * (xWidth / 2.0)
        xMax = xCenter + 0.8 * (xWidth / 2.0)
        if self.get_agent_pos(key)[0] > xMin:
            if self.get_agent_pos(key)[0] < xMax:
                return True
        else:
            return False
    def isSpeedHighConfidence(self,key):
        if self.asteroids[key].P[2][2] < 0.001:
            if self.asteroids[key].P[3][3] < 0.001:
                return True
        return False

    def isGoingUp(self,key):
        if self.asteroids[key].x[3][0] > 0:
            return True

    def get_agent_pos(self,key):
        x = self.asteroids[key].F * self.asteroids[key].x
        return (x[0][0], x[1][0])

    def get_distance(self,pos1,pos2):
        xdiff = abs(pos2[0] - pos1[0])
        ydiff = abs(pos2[1] - pos1[1])
        return math.sqrt(xdiff * xdiff + ydiff * ydiff)

    def jump(self, asteroid_observations, agent_data):
        """ Return the id of the asteroid the spaceship should jump/hop onto in the next timestep
        ----------
        self = a reference to the current object, the Spaceship
        asteroid_observations: Same as predict_from_observations method
        agent_data: a dictionary containing agent related data:
        'jump_distance' - a float representing agent jumping distance,
        'ridden_asteroid' - an int representing the ID of the ridden asteroid if available, None otherwise.
        Note: 'agent_pos_start' - A tuple representing the (x, y) position of the agent at t=0 is available in the constructor.

        agent_data format:
        {'ridden_asteroid': None,
         'jump_distance': agent.jump_distance,
         }
        Returns
        -------
        You are to return two items.
        1: idx, this represents the ID of the asteroid on which to jump if a jump should be performed in the next timestep.
        Return None if you do not intend to jump on an asteroid in the next timestep
        2. Return the estimated positions of the asteroids (i.e. the output of 'predict_from_observations method)
        IFF you intend to have them plotted in the visualization. Otherwise return None
        -----
        an example return
        idx to hop onto in the next timestep: 3,
        estimated_results = {1: (x-coordinate, y-coordinate),
          2: (x-coordinate, y-coordinate)}

        return 3, estimated_return

        """
        # FOR STUDENT TODO: Update the idx of the asteroid on which to jump
        asteroidsPos = self.predict_from_observations(asteroid_observations)
        if agent_data['ridden_asteroid'] != None:
            self.shipX = self.get_agent_pos(agent_data['ridden_asteroid'])[0]
            self.shipY = self.get_agent_pos(agent_data['ridden_asteroid'])[1]
        shipPos = (self.shipX,self.shipY)
        if self.win == True:
            return None, asteroidsPos
        if self.shipY >= self.y_bounds[1]:
            self.win = True
            return None, asteroidsPos

        ### get list of agents within jumping distance and high confidence speed
        nearAsteroids = []
        for agent in self.asteroids.keys():
            agentPos = self.get_agent_pos(agent)
            distanceToShip = self.get_distance(agentPos,shipPos)
            if distanceToShip < agent_data['jump_distance'] * 0.8:
                if self.isSpeedHighConfidence(agent):
                    if self.isGoingUp(agent):
                        if self.isWithinHorizontalBounds(agent):
                            if self.isWithinVerticalBounds(agent):
                                nearAsteroids.append(agent)
        if len(nearAsteroids) > 0:
            idx = nearAsteroids[0]
        else:
            idx = None
        xCenter = (self.x_bounds[0] + self.x_bounds[1])  / 2
        xWidth = abs(self.x_bounds[0] - self.x_bounds[1])
        xMin = xCenter - 0.2 * (xWidth / 2.0)
        xMax = xCenter + 0.2 * (xWidth / 2.0)
        if self.shipX > xMax:
            for asteroid in nearAsteroids:
                if self.asteroids[asteroid].x[2][0] < 0:
                    idx = asteroid
                    break;
        if self.shipX < xMin:
            for asteroid in nearAsteroids:
                if self.asteroids[asteroid].x[2][0] > 0:
                    idx = asteroid
                    break;

        xMin = xCenter - 0.8 * (xWidth / 2.0)
        xMax = xCenter + 0.8 * (xWidth / 2.0)
        if self.shipX > xMax:
            nearAsteroids = []
            for agent in self.asteroids.keys():
                agentPos = self.get_agent_pos(agent)
                distanceToShip = self.get_distance(agentPos, shipPos)
                if distanceToShip < agent_data['jump_distance'] * 0.8:
                    if self.isSpeedHighConfidence(agent):
                        nearAsteroids.append(agent)
            for asteroid in nearAsteroids:
                if self.asteroids[asteroid].x[2][0] < 0:
                    idx = asteroid
                    break;
        if self.shipX < xMin:
            nearAsteroids = []
            for agent in self.asteroids.keys():
                agentPos = self.get_agent_pos(agent)
                distanceToShip = self.get_distance(agentPos, shipPos)
                if distanceToShip < agent_data['jump_distance'] * 0.8:
                    if self.isSpeedHighConfidence(agent):
                        nearAsteroids.append(agent)
            for asteroid in nearAsteroids:
                if self.asteroids[asteroid].x[2][0] > 0:
                    idx = asteroid
                    break;
        if idx == agent_data['ridden_asteroid']:
            idx = None
        return idx, asteroidsPos

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith125).
    whoami = 'aelsabbagh3'
    return whoami