import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10, requires_grad=True)
torch.set_warn_always(True)