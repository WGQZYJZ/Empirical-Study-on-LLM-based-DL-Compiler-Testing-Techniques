import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
is_parametrized = torch.nn.utils.parametrize.is_parametrized(input_data)