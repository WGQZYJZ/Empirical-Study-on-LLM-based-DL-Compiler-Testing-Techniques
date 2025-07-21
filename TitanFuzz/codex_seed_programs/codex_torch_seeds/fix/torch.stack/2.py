'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
z = torch.stack([x, y])
print(z)