import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(4, 4)
output_data = torch.asin(input_data)