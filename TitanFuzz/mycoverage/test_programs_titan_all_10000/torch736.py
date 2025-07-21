import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([True, True, False, False])
y = torch.tensor([True, False, True, False])
z = torch.logical_xor(x, y)