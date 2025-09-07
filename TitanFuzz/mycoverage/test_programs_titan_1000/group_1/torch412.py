import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3, 4)
output_data = torch.atleast_2d(input_data)