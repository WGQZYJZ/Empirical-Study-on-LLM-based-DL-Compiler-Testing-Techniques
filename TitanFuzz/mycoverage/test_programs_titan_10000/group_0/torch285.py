import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.linspace((- 10), 10, steps=100)
output_data = torch.special.sinc(input_data)