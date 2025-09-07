import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 3, 4, 4)
y = torch.nn.functional.relu(x)