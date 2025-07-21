import torch
from torch import nn
from torch.autograd import Variable
window_length = 5
window = torch.hamming_window(window_length)