import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 3)
remainder_data = torch.remainder(input_data, 2)