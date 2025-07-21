import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5)
output = torch.Tensor.cov(input_data)