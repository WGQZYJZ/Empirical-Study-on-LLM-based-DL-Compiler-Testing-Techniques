import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[7, 8, 9]])
z = torch.tensor([[10, 11, 12]])
tensors = torch.atleast_1d(x, y, z)
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = torch.tensor([7, 8, 9])