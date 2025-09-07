import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 1, 4)
output_tensor = torch.atleast_2d(input_tensor)