import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
input_data = torch.randn(window_length)
output = torch.hamming_window(window_length)