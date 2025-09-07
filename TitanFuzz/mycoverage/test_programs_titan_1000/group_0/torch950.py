import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
other_data = torch.randn(5, 5)
output = torch.div(input_data, other_data)