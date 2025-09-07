import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 5)
flip_input = torch.flip(input, dims=[0])