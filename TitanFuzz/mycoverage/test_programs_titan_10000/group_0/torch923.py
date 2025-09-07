import torch
from torch import nn
from torch.autograd import Variable

window_length = 10
periodic = True
beta = 12.0
output = torch.kaiser_window(window_length, periodic, beta)