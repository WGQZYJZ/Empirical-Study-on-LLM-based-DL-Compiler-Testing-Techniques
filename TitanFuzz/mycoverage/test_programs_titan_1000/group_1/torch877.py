import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
output_data = torch.norm(input_data, p=2, dim=1)