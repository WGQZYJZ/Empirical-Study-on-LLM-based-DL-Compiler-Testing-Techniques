import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.set_printoptions(precision=1, threshold=1, edgeitems=2, linewidth=80, profile='full', sci_mode=False)
torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)