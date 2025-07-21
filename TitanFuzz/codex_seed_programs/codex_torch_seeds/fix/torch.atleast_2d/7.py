'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_2d\ntorch.atleast_2d(*tensors)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
a = torch.tensor(1)
b = torch.tensor([1, 2, 3])
c = torch.tensor([[1, 2, 3], [4, 5, 6]])
d = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('Task 3: Call the API torch.atleast_2d')
print(torch.atleast_2d(a))
print(torch.atleast_2d(b))
print(torch.atleast_2d(c))
print(torch.atleast_2d(d))