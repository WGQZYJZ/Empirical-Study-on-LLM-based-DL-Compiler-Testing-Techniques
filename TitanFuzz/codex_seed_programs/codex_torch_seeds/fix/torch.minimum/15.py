'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.minimum(x, y)
print(z)