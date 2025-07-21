import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
result = torch.flip(input_data, [1])