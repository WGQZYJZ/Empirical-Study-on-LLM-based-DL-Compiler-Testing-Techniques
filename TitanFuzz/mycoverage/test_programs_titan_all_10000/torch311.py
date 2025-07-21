import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([True, False, True])
y = torch.tensor([False, False, True])
z = torch.logical_and(x, y)