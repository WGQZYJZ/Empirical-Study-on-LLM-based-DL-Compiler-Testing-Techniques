import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
result = torch.Tensor.pow_(input_data, 2)