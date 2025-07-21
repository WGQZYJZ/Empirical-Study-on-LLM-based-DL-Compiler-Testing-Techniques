import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
real_tensor = torch.Tensor.real(input_tensor)