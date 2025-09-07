import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(4, 4)
result = torch.std(input_data, dim=1)