'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
import torch
x = torch.tensor([1, 2])
y = torch.tensor([[1, 1], [2, 2]])
z = torch.tensor([[[1, 1], [2, 2]], [[3, 3], [4, 4]]])
print(torch.atleast_3d(x))
print(torch.atleast_3d(y))
print(torch.atleast_3d(z))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_4d\ntorch.atleast_4d(*tensors)\n'
import torch
import torch
x = torch.tensor([1, 2])