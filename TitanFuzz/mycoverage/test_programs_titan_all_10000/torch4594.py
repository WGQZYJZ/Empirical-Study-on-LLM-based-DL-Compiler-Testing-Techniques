import torch
from torch import nn
from torch.autograd import Variable
inp = torch.randn(1, 1, 3, 3)
tanh = torch.nn.Tanh()
out = tanh(inp)