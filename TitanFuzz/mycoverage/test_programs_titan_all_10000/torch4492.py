import torch
from torch import nn
from torch.autograd import Variable
n = 10
low = 0
high = 100
x = torch.randint(low, high, (n,), dtype=torch.int64)