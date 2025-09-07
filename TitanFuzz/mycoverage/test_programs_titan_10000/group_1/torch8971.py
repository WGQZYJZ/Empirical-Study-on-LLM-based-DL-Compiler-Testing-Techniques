import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(4, 3)
output_data = torch.empty_like(input_data)