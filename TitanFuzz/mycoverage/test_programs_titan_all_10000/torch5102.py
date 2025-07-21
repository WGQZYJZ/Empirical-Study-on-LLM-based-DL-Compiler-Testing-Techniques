import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
torch.nn.functional.pdist(x, p=2)
torch.nn.functional.pdist(x, p=1)
torch.nn.functional.pdist(x, p=0.5)