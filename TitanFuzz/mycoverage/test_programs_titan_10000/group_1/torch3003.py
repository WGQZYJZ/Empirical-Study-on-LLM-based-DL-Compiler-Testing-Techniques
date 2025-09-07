import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(10)
sampler = torch.utils.data.Sampler(input_data)