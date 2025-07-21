import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10, 3)
torch.nn.functional.pdist(x, p=2)