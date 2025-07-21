'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
input = torch.rand(3, 4)
other = torch.rand(4, 5)
print(torch.linalg.matmul(input, other))