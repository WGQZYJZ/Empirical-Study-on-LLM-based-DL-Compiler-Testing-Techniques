import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
cosh_result = torch.cosh(input_data)