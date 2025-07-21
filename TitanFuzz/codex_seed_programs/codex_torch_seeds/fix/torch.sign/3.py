'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.sign(x)
print(x)
print(y)