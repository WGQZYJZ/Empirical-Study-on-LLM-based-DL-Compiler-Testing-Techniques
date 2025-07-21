'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
x = torch.tensor([1, 2, 3])
print(x)
y = torch.atleast_3d(x)
print(y)