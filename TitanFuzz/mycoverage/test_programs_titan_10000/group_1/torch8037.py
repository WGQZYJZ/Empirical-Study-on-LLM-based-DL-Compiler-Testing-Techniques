import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 3)
result_lt = torch.lt(input_data, 0.5)