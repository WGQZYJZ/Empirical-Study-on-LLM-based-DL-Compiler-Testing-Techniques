'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
x = torch.randn(1, 3)
print(x)
y = torch.positive(x)
print(y)
z = torch.clamp(x, min=(- 0.5), max=0.5)
print(z)