import torch
from torch import nn
from torch.autograd import Variable
window_length = 5
hann_window = torch.hann_window(window_length)