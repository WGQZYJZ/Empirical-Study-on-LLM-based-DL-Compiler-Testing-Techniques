import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
lgamma_tensor = torch.Tensor.lgamma_(input_tensor)