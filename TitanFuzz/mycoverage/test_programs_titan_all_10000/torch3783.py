import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
other_data = torch.rand(2, 3)
output = torch.divide(input_data, other_data)