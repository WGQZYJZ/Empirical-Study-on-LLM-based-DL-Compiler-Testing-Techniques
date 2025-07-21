import torch
from torch import nn
from torch.autograd import Variable
A = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.Tensor([1, 2, 3])
x = torch.Tensor.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)