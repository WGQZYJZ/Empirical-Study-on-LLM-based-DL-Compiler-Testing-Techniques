import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(0, 18, dtype=torch.float32).reshape(3, 2, 3)
y = torch.tile(x, (2, 3, 1))