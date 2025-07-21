import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3)
other_data = torch.rand(1, 3)
output_data = torch.mul(input_data, other_data)