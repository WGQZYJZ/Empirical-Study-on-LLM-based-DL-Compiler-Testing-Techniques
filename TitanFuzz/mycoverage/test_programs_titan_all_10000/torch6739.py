import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
tanh_output = torch.nn.Tanh()(input_data)