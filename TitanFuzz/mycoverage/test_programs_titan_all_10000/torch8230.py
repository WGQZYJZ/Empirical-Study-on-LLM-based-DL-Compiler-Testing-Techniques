import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 5)
input_tensor[(0, 0)] = 0
input_tensor[(0, 1)] = 1
output_tensor = torch.Tensor.istft(input_tensor, n_fft=5, hop_length=1)