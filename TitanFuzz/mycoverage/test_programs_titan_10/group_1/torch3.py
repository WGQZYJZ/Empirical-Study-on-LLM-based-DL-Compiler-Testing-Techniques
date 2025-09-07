import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 1, 10)
torch.Tensor.istft(input_data, n_fft=10, hop_length=10, win_length=10, window=torch.ones(10), center=True, normalized=False, onesided=True, length=10, return_complex=False)