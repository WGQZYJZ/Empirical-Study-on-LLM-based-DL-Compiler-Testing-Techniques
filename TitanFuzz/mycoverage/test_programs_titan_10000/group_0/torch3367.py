import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.arange(10)
output_data = torch.roll(input_data, 3)