import torch
from torch import nn
from torch.autograd import Variable

window_length = 10
hamming_window = torch.hamming_window(window_length)