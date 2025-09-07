import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 5)
output = torch.Tensor.isposinf(input_tensor)