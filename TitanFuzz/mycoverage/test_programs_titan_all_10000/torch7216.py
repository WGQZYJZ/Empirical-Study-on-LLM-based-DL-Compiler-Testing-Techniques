import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(10, dtype=torch.float32)
output_data = torch.hann_window(10, periodic=True)