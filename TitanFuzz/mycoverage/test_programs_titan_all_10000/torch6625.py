import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 4)
output = torch.zeros_like(input_data)