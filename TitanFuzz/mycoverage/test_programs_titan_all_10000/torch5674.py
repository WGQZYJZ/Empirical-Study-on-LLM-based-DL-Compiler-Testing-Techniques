import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
input_data2 = torch.randn(10, 10)
torch.cholesky_solve(input_data, input_data2, upper=False, out=None)