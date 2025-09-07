import torch
from torch import nn
from torch.autograd import Variable

x = torch.ones(2, 2, requires_grad=True)
with torch.no_grad():
    print(torch.is_grad_enabled())