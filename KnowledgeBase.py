class KnowledgeBase:
    #here lie all fundamental and stylistic rules according to harmony and counterpoint principles.
    
    def __init__(self):
        pass
                                    #Single-voice motion description:
    
    def lap(self, nodeA, nodeB):
        #The distance between two successive notes in the same voice.
        #remember that lists start counting from 0.
        #so we need to add 1 in order to print the interval as it should be
        #according to harmony rules
        if(nodeA.getCoordinateY() != nodeB.getCoordinateY()):
            return ( abs( nodeA.getCoordinateX() - nodeB.getCoordinateX() ) +1 )
        else:
            print('note A:',nodeA.getCoordinates(),' and note B:', nodeB.getCoordinates(),' are not in different measures.')
            return -1
    
    #describing the direction of a single melody
    #The melody goes from a low note to a higher note, or from a high note to a lower note.
    
    def stepwiseMotion(self, startNode, targetNode):
        #the melody moves between neighboring notes in lap of 2
        return( self.lap(startNode, targetNode) == 2)
        #return( abs(startNode.getCoordinateX() - targetNode.getCoordinateX()) == 1)

    def skipwiseMotion(self, startNode, targetNode):
        #the melody moves between notes that are not neighbor to each other
        return( self.lap(startNode, targetNode) > 2 )
        #return( abs(startNode.getCoordinateX() - targetNode.getCoordinateX()) > 1)
    
    def repetitiveMotion(self, startNode, targetNode):
        #the melody repeats the same note 
        return( self.lap(startNode, targetNode) == 1 )
    
    def ascendingMotion(self, startNode, targetNode):
        #The melody is moving upwards.
        return ( targetNode.getCoordinateX() < startNode.getCoordinateX() )

    def descendingMotion(self, startNode, targetNode):
        #The melody is moving downwards.
        return (targetNode.getCoordinateX() > startNode.getCoordinateX() )
    
    def symmetricMotion(self, ListMelodyPathA, intCurrentPosition):
        #The melody makes a skipwise motion from one direction and then a stepwise motion to the opposite and vice versa
        if(intCurrentPosition < len(ListMelodyPathA)-2):
            return ( (self.skipwiseMotion(ListMelodyPathA[intCurrentPosition], ListMelodyPathA[intCurrentPosition+1])
                    and self.stepwiseMotion(ListMelodyPathA[intCurrentPosition+1], ListMelodyPathA[intCurrentPosition+2]))
                    
                    or
                    
                    (self.stepwiseMotion(ListMelodyPathA[intCurrentPosition], ListMelodyPathA[intCurrentPosition+1])
                    and self.skipwiseMotion(ListMelodyPathA[intCurrentPosition+1], ListMelodyPathA[intCurrentPosition+2]))
                    )
        else:
            return False
    
                                            #two voices
    
    def interval(self, nodeA, nodeB):
        #remember that lists start counting from 0.
        #so we need to add 1 in order to print the interval as it should be
        #according to harmony rules
        if(nodeA.getCoordinateY() == nodeB.getCoordinateY()):
            return ( abs( nodeA.getCoordinateX() - nodeB.getCoordinateX() ) +1 )
        else:
            print('note A and note B are not in same measure.')

    def similarMotion(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        #The direction of each melody is the same, but the intervals between the melodies are not.
        return (
            ( self.ascendingMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
             and self.ascendingMotion( ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition] ) )
            
            or
            
            ( self.descendingMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
            and self.descendingMotion(ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition]))
            
            and
            
            self.interval(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition-1]) != self.interval(ListMelodyPathA[intCurrentPosition], ListMelodyPathB[intCurrentPosition])
            )
    
    def parallelMotion(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        #A sub-category of similar motion where the interval between the melodies is the same.
        return (
            ( self.ascendingMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
             and self.ascendingMotion( ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition] ) )
            
            or
            
            ( self.descendingMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
            and self.descendingMotion(ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition]))
            
            and
            
            self.interval(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition-1]) == self.interval(ListMelodyPathA[intCurrentPosition], ListMelodyPathB[intCurrentPosition])
            )

    def contraryMotion(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        #contrary (two notes moving to different direction
        return (
            ( self.ascendingMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
             and self.descendingMotion(ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition] )
            or ( self.descendingMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
            and self.ascendingMotion(ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition])))
            )
    
    def obliqueMotion(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        #One voice moves up or down and the other voice sings the same note
        #there is no restriction to its use, although melody should be interesting
        #thus it shouldn't be stable for many measures. In this context 2 measures will be just fine
        
        return ( (self.repetitiveMotion(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathA[intCurrentPosition])
                and ListMelodyPathB[intCurrentPosition-1].getCoordinateX() != ListMelodyPathB[intCurrentPosition].getCoordinateX())
                
                or
                
                (self.repetitiveMotion(ListMelodyPathB[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition])
                and ListMelodyPathA[intCurrentPosition-1].getCoordinateX() != ListMelodyPathA[intCurrentPosition].getCoordinateX())
                )
        # counter = 0
        # for i in range(len(ListMelodyPathA)):
        #     if( ListMelodyPathA[intCurrentPosition-1].getCoordinateX() == ListMelodyPathA[intCurrentPosition].getCoordinateX()
        #         and ListMelodyPathB[intCurrentPosition-1].getCoordinateX() != ListMelodyPathB[intCurrentPosition].getCoordinateX() ):
        #         counter = counter  + 1
        #     else:
        #         counter = 0
        # return (counter > 7)
        
    def unison(self, nodeA, nodeB):
        #unison is not allowed in the middle of the music piece.
        #Just in the beginning and in the end of the 8-measured piece
        return self.interval(nodeA, nodeB) == 1
        # return ( (nodeA.getCoordinateY() > 0 or nodeA.getCoordinateY() < 7)\
        #     and self.interval(nodeA, nodeB) == 1)
    
    
                                                        #rules
                                                        
    #fundamental rules
    def consecutiveFifths(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        return(
                (
                    (
                        self.contraryMotion (ListMelodyPathA, ListMelodyPathB, intCurrentPosition-1)
                        or self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition-1)
                        or ListMelodyPathA[intCurrentPosition-1].getCoordinateY()==ListMelodyPathB[intCurrentPosition-1].getCoordinateY() == 0   
                    )
                    and self.interval(ListMelodyPathA[intCurrentPosition], ListMelodyPathB[intCurrentPosition]) == 5
                )
            or
                (
                self.interval(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition-1]) == 5
                and self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition)
                )
            )

    def parallelFifths(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        return ( self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition) and
                self.interval(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition-1]) == self.interval(ListMelodyPathA[intCurrentPosition], ListMelodyPathB[intCurrentPosition]) == 5
                )

    def consecutiveEights(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        return(
                (
                    (
                        self.contraryMotion (ListMelodyPathA, ListMelodyPathB, intCurrentPosition-1)
                    or self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition-1)
                    or ListMelodyPathA[intCurrentPosition-1].getCoordinateY()==ListMelodyPathB[intCurrentPosition-1].getCoordinateY() == 0   
                    )
                    and self.interval(ListMelodyPathA[intCurrentPosition], ListMelodyPathB[intCurrentPosition]) == 8
                )
            or
                (
                self.interval(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition-1]) == 8
                and self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition)
                )
            )
    
    def parallelEights(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
        return ( self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition) and
                self.interval(ListMelodyPathA[intCurrentPosition-1], ListMelodyPathB[intCurrentPosition-1]) == self.interval(ListMelodyPathA[intCurrentPosition], ListMelodyPathB[intCurrentPosition]) == 8
                )
    
    def crossing(self, ListMelodyPathA, ListMelodyPathB, intCurrentPosition):
		#in music theory, voice crossing is the intersection of melodic lines in a composition,
        #leaving a lower voice on a higher pitch than a higher voice (and vice versa).
        
        #in algorithm, the current position X of Cantus Firmus (melody B) must not be grater than X of contrapuntal melody (melody A)
        return (self.parallelMotion(ListMelodyPathA, ListMelodyPathB, intCurrentPosition)
        and ListMelodyPathB[intCurrentPosition].getCoordinateX() < ListMelodyPathA[intCurrentPosition-1].getCoordinateX()
        )
    
    #stylistic notes
    # def leapOfSeven(self, ListMelodyPath, intCurrentPosition):
    #     return(self.skipwiseMotion(ListMelodyPath[intCurrentPosition-1], ListMelodyPath[intCurrentPosition])
    #            and self.interval(ListMelodyPath[intCurrentPosition-1], ListMelodyPath[intCurrentPosition]) == 7)
    
    def highLeaps(self, ListMelodyPath, intCurrentPosition):
        return(self.skipwiseMotion(ListMelodyPath[intCurrentPosition-1], ListMelodyPath[intCurrentPosition])\
               and self.interval(ListMelodyPath[intCurrentPosition-1], ListMelodyPath[intCurrentPosition]) > 8)
    
    
    def consecutiveThirds(self, ListMelodyPathA, ListMelodyPathB):
        #no more than 3 interval of thirds in a row
        counter = 0
        for i in range(len(ListMelodyPathA)):
            if( self.parallelMotion(ListMelodyPathA, ListMelodyPathB, i) and self.interval(ListMelodyPathA[i], ListMelodyPathB[i]) == 3 ):
                counter = counter  + 1
            else:
                counter = 0
        return (counter > 7)

    def consecutiveSixths(self, ListMelodyPathA, ListMelodyPathB):
        counter = 0
        for i in range(len(ListMelodyPathA)):
            if( self.parallelMotion(ListMelodyPathA, ListMelodyPathB, i)  and self.interval(ListMelodyPathA[i], ListMelodyPathB[i]) == 6 ):
                counter = counter  + 1
            else:
                counter = 0
        return (counter > 7)