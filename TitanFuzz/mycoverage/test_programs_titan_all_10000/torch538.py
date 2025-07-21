import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 1, 5, 5)
quantized_data = torch.quantize_per_tensor(input_data, scale=0.5, zero_point=3, dtype=torch.quint8)