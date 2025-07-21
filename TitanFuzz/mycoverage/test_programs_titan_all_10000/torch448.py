import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand((1, 3, 224, 224))
output = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
input = torch.rand((1, 3, 224, 224))