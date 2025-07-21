'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(3, 2)
output = torch.matmul(input, other)
print(output)