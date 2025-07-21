import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1)
output = torch.sinh(input_data)