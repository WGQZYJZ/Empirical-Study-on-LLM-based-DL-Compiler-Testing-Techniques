import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.nn.functional.relu(x)
y = torch.nn.functional.relu(x, inplace=True)