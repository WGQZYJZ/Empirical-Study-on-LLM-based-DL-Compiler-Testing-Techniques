import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
A = torch.randn(3, 3)
output_tensor = torch.Tensor.solve(input_tensor, A)