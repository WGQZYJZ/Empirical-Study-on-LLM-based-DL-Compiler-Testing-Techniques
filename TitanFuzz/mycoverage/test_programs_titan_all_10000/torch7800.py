import torch
from torch import nn
from torch.autograd import Variable
low = 0
high = 10
size = (2, 2)
out = torch.randint(low=low, high=high, size=size)