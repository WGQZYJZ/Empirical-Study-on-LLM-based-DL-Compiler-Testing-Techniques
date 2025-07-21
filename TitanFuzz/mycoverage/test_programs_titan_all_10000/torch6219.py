import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
torch.hann_window(window_length)