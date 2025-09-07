import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.arange(0, 5)
exponent = 2
result = torch.Tensor.pow_(input_tensor, exponent)