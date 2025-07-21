import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(3, 3, 3)
fft_data = torch.fft.rfftn(data)