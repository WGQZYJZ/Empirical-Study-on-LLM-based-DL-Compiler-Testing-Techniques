'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6])
print(x)
print(torch.atleast_2d(x))
print(x.view(2, 3))