import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 4)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=False)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=True)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=False)
torch.set_printoptions(precision=10, threshold=100000, edgeitems=2, linewidth=1000, profile='full', sci_mode=True)