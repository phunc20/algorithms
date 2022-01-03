import imagematrix

class ResizeableImage(imagematrix.Bild):
    def best_seam(self):
        # Construct dp, i.e. the accumulation energy matrix by dynamic programming
        n_rows, n_cols = self.array.shape[:2]
        dp = np.empty(shape=(n_rows, n_cols))
        for j in range(self.width):
            dp[0, j] = self.energy(0, j)
        for i in range(1, self.height):
            for j in range(self.width):
                start = max(0, j-1)
                end = min(self.width-1, j+1)
                dp[i, j] =  self.energy(i, j) + \
                        min(dp[i-1, col] for col in range(start, end+1))
        # Find the least-energy seam in dp,
        # starting from the bottom-most row
        seam = []
        minimum = float("inf")
        for j in range(self.width):
            present = dp[self.height-1, j]
            if  present < minimum:
                col_idx = j
                minimum = present
        seam.append((self.height-1, col_idx))
        for i in range(self.height-1, 0, -1):
            j = seam[-1][1]
            minimum = float("inf")
            start = max(0, j-1)
            end = min(self.width-1, j+1)
            for jj in range(start, end+1):
                present = dp[i-1, jj]
                if  present < minimum:
                    col_idx = jj
                    minimum = present
            seam.append((col_idx, j-1))
        return seam

    def remove_best_seam(self):
        # remove_seam() has already been implemented in imagematrix.py
        self.remove_seam(self.best_seam())
