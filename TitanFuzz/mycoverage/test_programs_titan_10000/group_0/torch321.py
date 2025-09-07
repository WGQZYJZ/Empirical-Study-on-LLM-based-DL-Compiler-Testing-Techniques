import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(3, 4)
res = torch.Tensor.lgamma(input_data)