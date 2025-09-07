import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.Tensor.random_(input_data, from_=0, to=None, generator=None)