import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(2, 2, requires_grad=True)
torch.is_warn_always_enabled()