import torch
from torch import nn
from torch.autograd import Variable
size = (2, 3, 4)
stride = (1, 2, 3)
out = torch.empty_strided(size, stride)