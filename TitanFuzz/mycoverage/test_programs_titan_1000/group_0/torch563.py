import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3, 4)
real_tensor = torch.Tensor.real(input_tensor)