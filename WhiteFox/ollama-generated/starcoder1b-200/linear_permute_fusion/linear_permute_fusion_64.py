
# Test Cases for this Model
For each test case:
- input tensor
  - shape 2
  - value of '0' (no permute)
- input tensor
  - shape 3 with a single value between [-1, 1] (one to one permute), and a single value between [-1, 1], and a single value between [1, 1] (two to two permutations), i.e. the first row is '[-1, -1]', and the second row is '[1, 1]'
- input tensor
  - shape 3 with the last column as 0 and the first column as 0
- input tensor
  - shape 4 with a single value between [-2, 2], and the third column of this matrix as 0
- input tensor
  - shape 4 with a single value between [-1.5, 1.5] and the second row as [1, 1]

