import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2)
tanh_output = torch.nn.Tanh()