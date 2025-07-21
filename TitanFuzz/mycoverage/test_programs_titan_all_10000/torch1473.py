import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 1, 2, 1, 2)
squeeze_data = torch.squeeze(input_data)