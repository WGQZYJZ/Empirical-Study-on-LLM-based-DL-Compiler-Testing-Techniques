import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([True, False, True, True], dtype=torch.bool)
y = torch.logical_not(x)