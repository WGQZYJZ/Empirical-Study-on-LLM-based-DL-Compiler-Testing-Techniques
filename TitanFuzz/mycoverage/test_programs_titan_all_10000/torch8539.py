import torch
from torch import nn
from torch.autograd import Variable
low = 1
high = 100
size = (3, 3)
a = torch.randint(low, high, size)