import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
softplus_output = torch.nn.functional.softplus(input_data)