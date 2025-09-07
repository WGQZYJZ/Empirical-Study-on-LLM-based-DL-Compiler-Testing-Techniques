import torch
from torch import nn
from torch.autograd import Variable

data = torch.randn(2, 3)
torch.random.manual_seed(7)
data = torch.randn(2, 3)
torch.random.manual_seed(7)
data = torch.randn(2, 3)