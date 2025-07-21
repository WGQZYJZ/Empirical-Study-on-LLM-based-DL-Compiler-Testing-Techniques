import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([True, False, True, False])
y = torch.logical_not(x)