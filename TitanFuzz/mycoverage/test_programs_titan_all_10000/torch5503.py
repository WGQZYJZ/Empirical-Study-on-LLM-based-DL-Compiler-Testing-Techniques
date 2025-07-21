import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.triangular_solve(input_tensor, A, upper=True, transpose=False, unitriangular=False)
torch.Tensor.triangular_solve(input_tensor, A, upper=False, transpose=False, unitriangular=False)
torch.Tensor.triangular_solve(input_tensor, A, upper=True, transpose=True, unitriangular=False)
torch.Tensor.triangular_solve(input_tensor, A, upper=False, transpose=True, unitriangular=False)