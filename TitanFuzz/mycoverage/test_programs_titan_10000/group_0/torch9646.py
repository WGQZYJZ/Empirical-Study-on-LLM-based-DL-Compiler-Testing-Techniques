import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(1, requires_grad=True)
output_data = torch.rand(1, requires_grad=True)