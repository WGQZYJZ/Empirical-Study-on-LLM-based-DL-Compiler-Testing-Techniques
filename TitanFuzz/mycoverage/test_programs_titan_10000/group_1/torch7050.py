import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(100)
histogram_result = torch.Tensor.histogram(input_data, bins=3, range=((- 1), 1))