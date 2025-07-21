import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
generator = torch.Generator(device='cpu')