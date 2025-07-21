'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
y = torch.expm1(x)
print(y)
'\nTask 4: Call the API torch.expm1_\ntorch.expm1_(input)\n'
torch.expm1_(x)
print(x)