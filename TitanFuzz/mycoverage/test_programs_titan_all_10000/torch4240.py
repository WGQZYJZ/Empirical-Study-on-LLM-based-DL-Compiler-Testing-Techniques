import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
quantized_tensor = torch.quantize_per_tensor(input_tensor, scale=1.0, zero_point=0, dtype=torch.quint8)