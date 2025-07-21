import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
A = torch.randn(5, 5)
torch.Tensor.solve(input_tensor, A)