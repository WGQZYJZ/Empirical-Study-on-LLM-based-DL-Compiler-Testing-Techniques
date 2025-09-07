import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
digamma_data = torch.digamma(input_data)