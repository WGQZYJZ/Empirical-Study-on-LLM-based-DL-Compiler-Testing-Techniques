import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3)
torch.hamming_window(3, periodic=True)
torch.hamming_window(3, periodic=False)
torch.hamming_window(3, periodic=True, alpha=0.54, beta=0.46)
torch.hamming_window(3, periodic=False, alpha=0.54, beta=0.46)