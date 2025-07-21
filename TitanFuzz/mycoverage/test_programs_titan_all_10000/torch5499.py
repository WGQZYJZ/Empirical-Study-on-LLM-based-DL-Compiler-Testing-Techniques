import torch
from torch import nn
from torch.autograd import Variable
window_length = 10
window = torch.bartlett_window(window_length)