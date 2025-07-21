import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 1, 3, 3, 3)
padding = (1, 1, 1, 1, 1, 1)
value = 0
result = torch.nn.ConstantPad3d(padding, value)(data)