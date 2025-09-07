import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(3, 3)
remainder = torch.remainder(input_data, 2)