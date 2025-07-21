'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print(input)
other = torch.randn(3, 4)
print(other)
out = torch.linalg.matmul(input, other)
print(out)
out = torch.matmul(input, other)
print(out)