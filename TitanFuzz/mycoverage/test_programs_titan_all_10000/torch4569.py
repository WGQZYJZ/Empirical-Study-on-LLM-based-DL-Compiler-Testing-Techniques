import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(4, 4)
other_data = torch.rand(4, 4)
output_data = torch.copysign(input_data, other_data)