import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([True, False, True], dtype=torch.bool)
y = torch.tensor([True, False, False], dtype=torch.bool)
z = torch.logical_or(x, y)