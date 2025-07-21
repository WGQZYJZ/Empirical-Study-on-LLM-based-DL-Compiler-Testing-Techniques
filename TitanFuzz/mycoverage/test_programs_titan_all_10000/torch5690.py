import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
output = torch.reciprocal(input_data)
output = torch.reciprocal(input_data, out=input_data)