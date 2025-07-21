'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[7, 8, 9]])
z = torch.tensor([[10, 11, 12]])
tensors = torch.atleast_1d(x, y, z)
print(tensors)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = torch.tensor([7, 8, 9])