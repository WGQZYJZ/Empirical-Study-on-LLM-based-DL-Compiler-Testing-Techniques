import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(2, 2)
y = torch.randn(2, 2)
torch.overrides.handle_torch_function(torch.add, (x, y), x, y)