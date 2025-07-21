import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
A = torch.randn(4, 4)
output_tensor = torch.Tensor.solve(_input_tensor, A)