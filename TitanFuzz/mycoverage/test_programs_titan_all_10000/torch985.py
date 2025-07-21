import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
sqrt_data = torch.sqrt(input_data)