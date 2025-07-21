import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
y = torch.randn(3, 3)
z = torch.randn(3, 3)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=2, profile=None, sci_mode=None)