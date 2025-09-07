import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
output = torch.blackman_window(window_length)