'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
output = torch.matmul(input, input.t())
print(output)