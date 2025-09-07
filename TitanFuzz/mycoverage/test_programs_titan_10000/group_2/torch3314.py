import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(16, dtype=torch.float32).reshape(2, 8)
y = torch.vsplit(x, 2)