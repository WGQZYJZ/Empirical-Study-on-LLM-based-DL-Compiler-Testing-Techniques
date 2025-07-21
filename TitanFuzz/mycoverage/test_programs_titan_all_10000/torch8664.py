import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
torch.ceil(input_data)
input_data = torch.randn(1, 2, 3)
torch.clamp(input_data, min=0.5, max=1.5)
input_data = torch.randn(1, 2, 3)