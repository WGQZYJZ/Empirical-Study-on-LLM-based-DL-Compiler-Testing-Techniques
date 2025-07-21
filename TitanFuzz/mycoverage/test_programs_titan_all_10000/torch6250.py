import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(2, 3, dtype=torch.float)
torch.set_default_dtype(torch.float)
b = torch.randn(2, 3)