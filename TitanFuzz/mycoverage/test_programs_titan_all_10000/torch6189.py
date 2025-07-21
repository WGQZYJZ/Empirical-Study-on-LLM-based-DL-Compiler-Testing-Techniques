import torch
from torch import nn
from torch.autograd import Variable
size = (3, 4)
stride = (3, 2)
out = torch.empty_strided(size, stride)