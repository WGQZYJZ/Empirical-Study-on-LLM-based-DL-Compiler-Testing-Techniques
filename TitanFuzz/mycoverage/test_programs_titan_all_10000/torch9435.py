import torch
from torch import nn
from torch.autograd import Variable
size = (4, 4)
fill_value = 0.5
output = torch.full(size, fill_value)