'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
x = torch.Tensor([1, 2, 3])
y = torch.Tensor([4, 5, 6])
z = torch.Tensor([7, 8, 9])
print(torch.stack((x, y, z)))
print(torch.stack((x, y, z), dim=1))
print(torch.stack((x, y, z), dim=0))