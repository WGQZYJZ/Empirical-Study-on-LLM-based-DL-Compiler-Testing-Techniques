import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
tanh = torch.nn.Tanh()
output = tanh(input_data)