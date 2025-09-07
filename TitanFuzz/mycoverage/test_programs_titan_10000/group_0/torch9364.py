import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(1, 5)
tanh_out = torch.nn.Tanh()(input_data)