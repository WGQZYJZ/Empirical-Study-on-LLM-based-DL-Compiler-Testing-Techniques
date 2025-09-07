import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(3, 3)
g = torch.Generator(device='cpu')