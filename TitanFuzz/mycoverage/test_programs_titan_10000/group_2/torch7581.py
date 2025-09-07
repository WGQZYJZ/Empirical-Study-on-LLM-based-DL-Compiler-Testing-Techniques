import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(1, 6, dtype=torch.float)
y = torch.arange(1, 6, dtype=torch.float)
z = torch.Tensor.outer(x, y)