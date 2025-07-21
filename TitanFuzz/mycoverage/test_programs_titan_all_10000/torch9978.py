import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
output = torch.blackman_window(input_data.shape[0])