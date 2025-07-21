import torch
from torch import nn
from torch.autograd import Variable
inp = torch.randn(1, 1, 2, 2)
torch.overrides.is_tensor_like(inp)
torch.overrides.is_tensor_like(inp.tolist())