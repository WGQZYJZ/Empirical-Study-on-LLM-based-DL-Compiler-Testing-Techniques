import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
output = torch.Tensor.t(input_tensor)