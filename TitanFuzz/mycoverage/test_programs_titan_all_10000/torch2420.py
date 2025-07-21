import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 1, 4, 4)
unfold = torch.nn.Unfold(kernel_size=(2, 2))
output = unfold(input_data)