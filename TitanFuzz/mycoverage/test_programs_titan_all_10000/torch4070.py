import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100, 100)
output = torch.rad2deg(input_data)