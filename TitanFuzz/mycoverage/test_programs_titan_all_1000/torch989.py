import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 3, 3)
output = torch.hamming_window(3, periodic=True)