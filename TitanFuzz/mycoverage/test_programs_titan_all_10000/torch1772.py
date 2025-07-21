import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
input_data = torch.rand(window_length)
output = torch.hann_window(window_length)