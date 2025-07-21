import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(5, 3, dtype=torch.double)
y = torch.randn_like(x, dtype=torch.float)
z = torch.randn_like(x, dtype=torch.double)