import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
torch.jit.unused(input_data)