import torch
from torch import nn
from torch.autograd import Variable

size = (2, 3)
fill_value = 2.0
out = torch.full(size, fill_value)