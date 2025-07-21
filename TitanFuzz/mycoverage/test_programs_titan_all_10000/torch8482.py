import torch
from torch import nn
from torch.autograd import Variable
window_length = 3
output = torch.blackman_window(window_length)