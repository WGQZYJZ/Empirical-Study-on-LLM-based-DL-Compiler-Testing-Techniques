import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(10)
window = torch.hann_window(10)
output = (input_data * window)