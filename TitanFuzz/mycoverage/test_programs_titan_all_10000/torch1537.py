import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
output = torch.special.ndtri(input_data)