import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 5)
other_data = torch.rand(5, 5)
output = torch.div(input_data, other_data)