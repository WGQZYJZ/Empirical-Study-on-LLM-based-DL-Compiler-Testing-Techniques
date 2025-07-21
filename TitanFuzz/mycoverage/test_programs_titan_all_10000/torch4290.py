import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3)
torch.nn.Tanh()(x)
torch.nn.functional.tanh(x)