import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 1, 3)
torch.Tensor.istft(input_tensor, n_fft=4)