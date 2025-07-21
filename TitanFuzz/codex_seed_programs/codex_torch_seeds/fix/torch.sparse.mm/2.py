'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.mm\ntorch.sparse.mm(mat1, mat2)\n'
import torch
(N, K, M) = (10, 10, 10)
mat1 = torch.randn(N, K)
mat2 = torch.randn(K, M)
output = torch.sparse.mm(mat1, mat2)
print(output)