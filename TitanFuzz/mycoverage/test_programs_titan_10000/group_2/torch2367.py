import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(4, 4)
output = torch.abs(input_data)