import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(4, 4)
torch.overrides.has_torch_function(x)