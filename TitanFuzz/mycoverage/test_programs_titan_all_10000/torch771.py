import torch
from torch import nn
from torch.autograd import Variable
size = (2, 3, 4)
stride = (8, 4, 2)
output = torch.empty_strided(size, stride)