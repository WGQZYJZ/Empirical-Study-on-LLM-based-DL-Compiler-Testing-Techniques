import torch
from torch import nn
from torch.autograd import Variable
window_length = 5
bartlett_window = torch.bartlett_window(window_length)