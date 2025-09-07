import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 4)
output_data = torch.lt(input_data, 0.5)