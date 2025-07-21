'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 2])
z = torch.tensor([1])
print(torch.atleast_1d(x, y, z))