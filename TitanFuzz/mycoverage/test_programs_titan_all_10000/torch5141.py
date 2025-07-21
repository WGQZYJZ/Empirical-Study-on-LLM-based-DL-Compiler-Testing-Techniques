import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3])
out = torch.vander(x, N=None, increasing=False)