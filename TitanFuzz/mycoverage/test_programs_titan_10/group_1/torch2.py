import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5)
output = torch.blackman_window(5)