'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(3, 4)
output = torch.linalg.matmul(input, other)
print(output)
output = torch.empty(2, 4)
torch.linalg.matmul(input, other, out=output)
print(output)