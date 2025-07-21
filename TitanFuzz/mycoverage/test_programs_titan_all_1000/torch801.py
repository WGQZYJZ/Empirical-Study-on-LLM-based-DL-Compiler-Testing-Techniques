import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, requires_grad=True)
output = torch.special.erfinv(input_data)