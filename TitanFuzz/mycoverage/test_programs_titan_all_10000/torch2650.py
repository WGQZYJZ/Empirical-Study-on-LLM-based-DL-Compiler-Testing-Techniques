import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
torch.set_printoptions(precision=5, threshold=5, edgeitems=5, linewidth=5, profile=None, sci_mode=None)
torch.set_printoptions(profile='default')