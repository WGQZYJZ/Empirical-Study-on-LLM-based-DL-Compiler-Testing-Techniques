import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(3, 4, 5)
torch.Tensor.istft(input_tensor, n_fft=10, hop_length=2)