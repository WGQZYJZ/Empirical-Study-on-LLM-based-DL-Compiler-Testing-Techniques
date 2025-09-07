import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[2, 1, 1], [1, 2, 1], [1, 1, 2]], dtype=torch.float)
b = torch.tensor([[1, 2, 3]], dtype=torch.float).t()
x = torch.triangular_solve(b, A, upper=True, transpose=False, unitriangular=False)