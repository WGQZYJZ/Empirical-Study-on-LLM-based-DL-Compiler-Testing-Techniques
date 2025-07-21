'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
A = torch.rand(2, 3)
B = torch.rand(3, 2)
print(torch.linalg.matmul(A, B))