import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
(LU_data, LU_pivots) = torch.lu(input_data)
b = torch.randn(3, 3)
out = torch.lu_solve(b, LU_data, LU_pivots)