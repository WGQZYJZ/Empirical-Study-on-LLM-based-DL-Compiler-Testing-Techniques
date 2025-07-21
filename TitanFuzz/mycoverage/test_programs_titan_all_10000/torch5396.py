import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
y = torch.hsplit(x, 2)