class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        
        counter = 0
        current_type = ''

        while queue and counter < len(senate):

            senator = queue.popleft()
            if current_type == '':
                counter = 1
                current_type = senator
                queue.append(senator)
            elif current_type == senator:
                counter += 1
                queue.append(senator)
            elif counter == 1:
                counter = 0
                current_type = ''
            else:
                counter -= 1


        return 'Radiant' if queue[0] == 'R' else 'Dire'
