import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 1, 1)
output_tensor = torch.squeeze(input_tensor)