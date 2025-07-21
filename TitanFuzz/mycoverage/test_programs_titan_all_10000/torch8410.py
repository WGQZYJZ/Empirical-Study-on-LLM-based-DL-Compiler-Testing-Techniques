import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
output = torch.randint_like(input_data, low=0, high=10)