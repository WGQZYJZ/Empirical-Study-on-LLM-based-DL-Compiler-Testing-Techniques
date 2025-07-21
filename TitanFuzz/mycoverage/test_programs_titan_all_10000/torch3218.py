import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
output_data = torch.bernoulli(input_data)
output_data = torch.bernoulli(input_data, generator=None, out=None)