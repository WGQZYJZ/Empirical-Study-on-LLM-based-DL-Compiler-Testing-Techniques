import torch
from torch import nn
from torch.autograd import Variable

in_data = torch.randn(10, dtype=torch.float32)
out_data = torch.fft.rfftfreq(in_data.size(0))