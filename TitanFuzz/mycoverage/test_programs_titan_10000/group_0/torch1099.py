import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 3)
y = torch.nn.ReLU()
y = torch.nn.ReLU(inplace=True)