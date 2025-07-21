import torch
from torch import nn
from torch.autograd import Variable
a = torch.ones(3)
b = torch.zeros(3)
c = torch.broadcast_tensors(a, b)