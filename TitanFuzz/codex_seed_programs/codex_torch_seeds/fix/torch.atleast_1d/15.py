'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
import torch
x = torch.tensor([1, 2, 3, 4])
y = torch.atleast_1d(x)
print(y)