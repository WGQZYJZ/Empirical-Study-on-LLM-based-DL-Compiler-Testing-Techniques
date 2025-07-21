import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output = torch.atan(input_data)
output = torch.atan_(input_data)