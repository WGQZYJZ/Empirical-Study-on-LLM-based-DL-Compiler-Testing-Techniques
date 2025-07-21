'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.add\ntorch.add(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.add(x, y)
print(z)