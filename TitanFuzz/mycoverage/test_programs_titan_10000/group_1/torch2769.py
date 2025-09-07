import torch
from torch import nn
from torch.autograd import Variable

inp = torch.randn(1, 3, 224, 224)
torch.overrides.is_tensor_like(inp)