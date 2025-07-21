import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
output = torch.deg2rad(input_data)