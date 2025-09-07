import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(100, 3)
result = torch.cov(input_data)