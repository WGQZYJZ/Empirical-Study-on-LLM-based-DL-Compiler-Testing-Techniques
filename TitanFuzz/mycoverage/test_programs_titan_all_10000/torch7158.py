import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
output = torch.reciprocal(input_data)