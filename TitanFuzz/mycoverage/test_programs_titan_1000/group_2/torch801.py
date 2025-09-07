import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(5, 5)
A = torch.randn(5, 5)
torch.Tensor.triangular_solve(_input_tensor, A, upper=True, transpose=False, unitriangular=False)