import torch
from torch import nn
from torch.autograd import Variable

window_length = 8
output = torch.bartlett_window(window_length)