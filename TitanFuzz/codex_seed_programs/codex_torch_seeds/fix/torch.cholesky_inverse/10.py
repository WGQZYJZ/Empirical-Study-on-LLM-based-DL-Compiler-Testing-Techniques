'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
B = torch.randn(3, 3)
B = (B @ B.T)
print(torch.cholesky_inverse(B))