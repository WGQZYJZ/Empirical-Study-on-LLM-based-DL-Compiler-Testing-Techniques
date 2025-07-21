import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3, requires_grad=True)
torch.random.manual_seed(1)
x = torch.rand(2, 3, requires_grad=True)
torch.random.manual_seed(1)
x = torch.rand(2, 3, requires_grad=True)