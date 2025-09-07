import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
svdvals = torch.linalg.svdvals(A)