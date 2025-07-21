import torch
from torch import nn
from torch.autograd import Variable
inp = torch.randn(3, 4)
torch.overrides.is_tensor_like(inp)