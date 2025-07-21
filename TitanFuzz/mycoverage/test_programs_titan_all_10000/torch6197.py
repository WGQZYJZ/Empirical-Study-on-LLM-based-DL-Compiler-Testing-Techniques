import torch
from torch import nn
from torch.autograd import Variable
tensor_input = torch.randn(4, 4)
tensor_output = torch.Tensor.arctanh_(tensor_input, out=None)