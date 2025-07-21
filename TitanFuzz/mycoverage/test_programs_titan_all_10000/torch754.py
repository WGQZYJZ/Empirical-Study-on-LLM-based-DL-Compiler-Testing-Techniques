import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, 3, 3)
quantized_input = torch.quantize_per_channel(input, scales=torch.tensor([1.0, 1.0, 1.0]), zero_points=torch.tensor([0, 0, 0]), axis=0, dtype=torch.quint8)