import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(6, dtype=torch.float).reshape(1, 1, 6)
padding = 2
value = 0
result = torch.nn.ConstantPad1d(padding, value)(data)