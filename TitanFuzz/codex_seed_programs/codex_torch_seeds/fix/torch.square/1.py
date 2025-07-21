'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
x = torch.rand(1, 3)
y = torch.square(x)
print(x)
print(y)
y = torch.sqrt(x)
print(y)
y = torch.rsqrt(x)
print(y)
y = torch.pow(x, 2)
print(y)
y = torch.exp(x)
print(y)