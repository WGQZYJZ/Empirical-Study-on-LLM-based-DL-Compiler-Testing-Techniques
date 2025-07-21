'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
x = torch.linspace(0, 10, steps=5)
print(x)
y = torch.sin(x)
print(y)