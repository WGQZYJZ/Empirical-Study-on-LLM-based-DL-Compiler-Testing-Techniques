import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 2)
output = torch.slogdet(input_data)