import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
scales = torch.tensor([0.1, 0.2, 0.3])
zero_points = torch.tensor([1, 2, 3])
output = torch.quantize_per_channel(input, scales, zero_points, 1, torch.quint8)