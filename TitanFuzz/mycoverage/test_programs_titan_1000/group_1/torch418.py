import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3)
y = torch.randn(1, 3)
z = torch.row_stack([x, y])