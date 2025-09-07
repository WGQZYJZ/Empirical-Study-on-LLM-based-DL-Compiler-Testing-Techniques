import torch
from torch import nn
from torch.autograd import Variable
input_size = (1, 3, 5, 5)
input_data = torch.randn(input_size)
torch.nn.init.orthogonal_(input_data)
input_size = (1, 3, 5, 5)
input_data = torch.randn(input_size)
torch.nn.init.orthogonal_(input_data, gain=2)