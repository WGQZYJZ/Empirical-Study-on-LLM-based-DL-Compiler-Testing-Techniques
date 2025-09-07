import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 1, 1, 1, dtype=torch.float32)
torch.polygamma(1, input)