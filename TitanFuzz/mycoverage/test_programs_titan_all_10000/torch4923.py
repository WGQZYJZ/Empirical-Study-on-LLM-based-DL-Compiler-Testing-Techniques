import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 3)
y = torch.broadcast_to(x, (2, 2))
z = torch.broadcast_tensors(x, torch.ones(2, 2))