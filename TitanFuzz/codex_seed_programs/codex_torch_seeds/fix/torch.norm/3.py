"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
x = torch.randn(2, 3)
print('Input data: \n', x)
y = torch.norm(x, dim=1, keepdim=True)
print('Output data: \n', y)