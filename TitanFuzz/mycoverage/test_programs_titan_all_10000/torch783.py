import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
output = torch.unbind(input_data, dim=0)