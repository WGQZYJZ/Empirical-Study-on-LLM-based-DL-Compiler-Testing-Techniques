import torch
from torch import nn
from torch.autograd import Variable
window_length = 3
result = torch.kaiser_window(window_length, periodic=True, beta=12.0)