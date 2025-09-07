import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(5, 3)
result = torch.neg(input_data)