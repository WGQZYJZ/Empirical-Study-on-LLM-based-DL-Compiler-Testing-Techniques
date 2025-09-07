import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(100)
y = torch.rand(100)
generator = torch.Generator(device='cpu')