import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(5, 5)
output = torch.sgn(input_data)