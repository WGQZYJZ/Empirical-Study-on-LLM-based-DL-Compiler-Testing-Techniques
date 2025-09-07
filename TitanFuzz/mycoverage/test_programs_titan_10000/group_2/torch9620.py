import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(2, 3)
torch.random.manual_seed(10)
x = torch.rand(2, 3)
torch.random.manual_seed(10)
x = torch.rand(2, 3)