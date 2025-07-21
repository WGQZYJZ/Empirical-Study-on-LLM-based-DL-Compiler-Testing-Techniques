import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 10)
output = torch.nn.functional.softplus(input_data)