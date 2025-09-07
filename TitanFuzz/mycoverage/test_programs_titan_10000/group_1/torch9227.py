import torch
from torch import nn
from torch.autograd import Variable

inp = torch.rand(3, 3)
torch.overrides.is_tensor_like(inp)