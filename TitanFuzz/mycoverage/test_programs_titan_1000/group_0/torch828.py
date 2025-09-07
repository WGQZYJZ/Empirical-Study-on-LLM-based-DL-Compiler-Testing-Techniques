import torch
from torch import nn
from torch.autograd import Variable
x = torch.empty(2, 3)
torch.nn.init.normal_(x)
torch.nn.init.normal_(x, mean=1.0)
torch.nn.init.normal_(x, std=2.0)
torch.nn.init.normal_(x, mean=1.0, std=2.0)
torch.nn.init.normal_(x, mean=2.0, std=2.0)