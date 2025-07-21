import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.linspace(start=0, end=10, steps=5)
output_data = torch.logspace(start=0, end=10, steps=5)