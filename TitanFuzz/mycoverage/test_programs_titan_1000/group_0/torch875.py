import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10, 1)
output_data = torch.atan(input_data)