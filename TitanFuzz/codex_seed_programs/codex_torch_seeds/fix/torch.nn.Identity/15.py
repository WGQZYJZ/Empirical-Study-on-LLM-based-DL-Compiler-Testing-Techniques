'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Identity\ntorch.nn.Identity(*args, **kwargs)\n'
import torch
x = torch.randn(2, 2)
print(x)
y = torch.nn.Identity(x)
print(y)