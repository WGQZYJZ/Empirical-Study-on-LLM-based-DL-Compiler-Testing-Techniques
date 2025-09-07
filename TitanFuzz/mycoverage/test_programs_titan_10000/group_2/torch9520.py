import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([True, False, True, False])
y = torch.tensor([True, True, False, False])
z = torch.bitwise_and(x, y)