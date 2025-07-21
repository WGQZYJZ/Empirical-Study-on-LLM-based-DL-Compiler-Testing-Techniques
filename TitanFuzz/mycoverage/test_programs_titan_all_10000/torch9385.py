import torch
from torch import nn
from torch.autograd import Variable
vec1 = torch.arange(1, 6)
vec2 = torch.arange(1, 4)
out = torch.outer(vec1, vec2)