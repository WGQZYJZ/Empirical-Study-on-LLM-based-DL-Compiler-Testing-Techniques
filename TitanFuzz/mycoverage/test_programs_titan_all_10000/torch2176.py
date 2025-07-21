import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
input2 = torch.randn(3, 4)
torch.Tensor.cholesky_solve(input_tensor, input2, upper=False)