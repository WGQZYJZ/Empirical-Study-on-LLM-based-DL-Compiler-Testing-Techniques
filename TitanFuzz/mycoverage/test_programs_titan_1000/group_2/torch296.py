import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([2.0, 4.0, 8.0, 16.0])
output = torch.rsqrt(input_data)