import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
flipped_data = torch.flipud(input_data)