import torch
from torch import nn
from torch.autograd import Variable

size = (4, 5)
stride = (5, 1)
result = torch.empty_strided(size, stride)