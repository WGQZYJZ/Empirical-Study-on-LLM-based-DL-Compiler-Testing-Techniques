import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1)
output = torch.Tensor.arctan(input_data)