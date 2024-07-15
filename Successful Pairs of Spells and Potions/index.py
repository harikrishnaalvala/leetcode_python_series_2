class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for i in range(0,len(spells)):
            x = ceil( success/spells[i]); 
            j = bisect.bisect_left(potions,x);
            res.append(len(potions)-j)
        
        return res
