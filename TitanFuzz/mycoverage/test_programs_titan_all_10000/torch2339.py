import torch
from torch import nn
from torch.autograd import Variable
inp = [1, 2, 3]
torch.overrides.is_tensor_like(inp)