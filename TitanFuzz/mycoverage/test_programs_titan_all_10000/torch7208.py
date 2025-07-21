import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 5)
output_data = torch.positive(input_data)