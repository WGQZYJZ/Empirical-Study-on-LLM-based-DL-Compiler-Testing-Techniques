import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
other_data = torch.rand(3, 3)
output_data = torch.special.gammainc(input_data, other_data)