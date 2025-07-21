import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.relu(x)