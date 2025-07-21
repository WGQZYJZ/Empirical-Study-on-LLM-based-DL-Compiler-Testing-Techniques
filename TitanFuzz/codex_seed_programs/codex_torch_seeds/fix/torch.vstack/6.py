'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
x = torch.arange(0, 9, dtype=torch.float32).view(3, 3)
print(x)
y = torch.arange(9, 18, dtype=torch.float32).view(3, 3)
print(y)
z = torch.vstack((x, y))
print(z)