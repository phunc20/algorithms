import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        # Construct dp, i.e. the accumulation energy matrix by dynamic programming
        dp = dict()
        for i in range(self.width):
            dp[i, 0] = self.energy(i, 0)
        for j in range(1, self.height):
            for i in range(self.width):
                #start = i - 1 if i > 0 else i
                #end = i + 1 if i < self.width - 1 else i
                start = max(0, i-1)
                end = min(self.width-1, i+1)
                dp[i, j] =  self.energy(i, j) + \
                        min(dp[col, j-1] for col in range(start, end+1))
        # Find the least-energy seam in dp,
        # starting from the bottom-most row
        seam = []
        minimum = float("inf")
        for i in range(self.width):
            present = dp[i, self.height-1]
            if  present < minimum:
                col_idx = i
                minimum = present
        seam.append((col_idx, self.height-1))
        for j in range(self.height-1, 0, -1):
            i = seam[-1][0]
            minimum = float("inf")
            start = max(0, i-1)
            end = min(self.width-1, i+1)
            for ii in range(start, end+1):
                present = dp[ii, j-1]
                if  present < minimum:
                    col_idx = ii
                    minimum = present
            seam.append((col_idx, j-1))
        return seam

    def remove_best_seam(self):
        # remove_seam() has already been implemented in imagematrix.py
        self.remove_seam(self.best_seam())
