import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 3, 3)
torch.linalg.svdvals(A)