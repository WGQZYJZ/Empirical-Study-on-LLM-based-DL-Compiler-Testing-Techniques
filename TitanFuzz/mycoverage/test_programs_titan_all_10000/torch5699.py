import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(3)
y = torch.broadcast_to(x, (4, 3))