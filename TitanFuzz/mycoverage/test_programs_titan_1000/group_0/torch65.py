import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
blackman_window = torch.blackman_window(window_length)