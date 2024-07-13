class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0

        # check first element
        maxAltitude=max(maxAltitude,gain[0])

        # Current altitute will be sum of current + previous
        for i in range(1,len(gain)):
            gain[i]=gain[i]+gain[i-1]

            # Check for max
            maxAltitude=max(maxAltitude,gain[i])

        # Return Max Altitude
        return maxAltitude
