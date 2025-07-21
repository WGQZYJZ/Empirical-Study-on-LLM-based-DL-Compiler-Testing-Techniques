import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, requires_grad=True)
cos_output = torch.cos(input_data)