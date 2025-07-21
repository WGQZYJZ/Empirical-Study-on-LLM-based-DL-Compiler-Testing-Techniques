import torch
from torch import nn
from torch.autograd import Variable
low = 0
high = 100
size = [2, 3]
data = torch.randint(low, high, size)
data = torch.randint(low, high, size, dtype=torch.float32)