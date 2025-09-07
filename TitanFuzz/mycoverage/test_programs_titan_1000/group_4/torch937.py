import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
other_data = torch.randn(1, 3)
output_data = torch.add(input_data, other_data)