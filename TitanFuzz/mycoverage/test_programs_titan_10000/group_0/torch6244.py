import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(5)
output = torch.hann_window(input_data.size(0))