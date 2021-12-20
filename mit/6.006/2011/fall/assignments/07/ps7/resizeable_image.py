import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        # Construct dp, i.e. the accumulation energy matrix by dynamic programming
        dp = dict()
        for i in range(self.width):
            dp[i, 0] = self.energy(i, 0)
        for j in range(self.height):
            for i in range(self.width):
                start = i - 1 if i > 0 else i
                end = i + 1 if i < self.width - 1 else i
                dp[i, j] =  self.energy(i, j) + \
                        min(dp[idx, j-1] for idx in range(start, end+1))
        # Find the least energy seam in dp,
        # starting from the bottom-most row
        raise NotImplemented

    def remove_best_seam(self):
        # remove_seam() has already been implemented in imagematrix.py
        self.remove_seam(self.best_seam())
