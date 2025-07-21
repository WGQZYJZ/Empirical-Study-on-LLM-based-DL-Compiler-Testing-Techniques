import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
torch.random.manual_seed(1)
y = torch.rand(5, 3)
torch.random.manual_seed(1)
z = torch.rand(5, 3)
torch.random.manual_seed(2)
a = torch.rand(5, 3)