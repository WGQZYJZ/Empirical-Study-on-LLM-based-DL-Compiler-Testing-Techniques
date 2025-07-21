import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
torch.Tensor.pow_(input_tensor, exponent=3)