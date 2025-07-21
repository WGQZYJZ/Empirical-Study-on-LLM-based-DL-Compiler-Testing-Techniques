import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
torch.broadcast_to(x, (3, 3))