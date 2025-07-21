import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3)
weights = torch.rand(3, 1)
output = torch.mm(input_data, weights)