class Solution:
    def insert(self, intervals, new):
        
        merged,t,l = [], 0, len(intervals)       
        for curr in intervals:
            
            # If interval[i] completely smaller than new one
            if new[0]>curr[1]:
                merged.append(curr)
             
            # If interval[i] completely greater than new
            elif curr[0]>new[1]:
                break
             
            # If interval[i] is overlapping with new
            else:              
                # choose minm and maxm boundaries from both
                new[0] = min(new[0], curr[0])
                new[1] = max(new[1], curr[1])
            
            t+=1
            
        # Apeending last new interval
        merged.append(new)
        
        # Now understand this part
        # i) If new part extend till end than simply return merged ones
        # ii) If not till end than return merged + remainling intervals
        return merged+intervals[t:] if t<l else merged
     