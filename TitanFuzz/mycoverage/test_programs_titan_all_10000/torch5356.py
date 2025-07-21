import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 1, 2, 1, 2)
output = torch.squeeze(input_data)
output = torch.squeeze(input_data, 0)
output = torch.squeeze(input_data, 1)