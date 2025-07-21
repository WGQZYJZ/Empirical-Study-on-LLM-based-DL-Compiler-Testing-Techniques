import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 21, dtype=torch.float32).reshape(1, 1, 4, 5)
unfold = torch.nn.Unfold(kernel_size=(2, 2), dilation=1, padding=0, stride=1)
output = unfold(input_data)