import torch
from torch import nn
from torch.autograd import Variable
window_length = 5
out = torch.blackman_window(window_length)