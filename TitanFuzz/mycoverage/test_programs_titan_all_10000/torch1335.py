import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, dtype=torch.float64)
torch.set_default_dtype(torch.float32)
torch.set_default_dtype(torch.float64)