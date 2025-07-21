'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
x = torch.tensor([0.0, 3.1415926, 6.28318531])
y = torch.cos(x)
print(y)