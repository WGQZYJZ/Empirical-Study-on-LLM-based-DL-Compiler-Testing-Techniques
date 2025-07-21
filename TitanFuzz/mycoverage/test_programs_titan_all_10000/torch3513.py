import torch
from torch import nn
from torch.autograd import Variable
n = 3
m = 4
eye = torch.eye(n, m)
size = (3, 4)
fill_value = 2
full = torch.full(size, fill_value)