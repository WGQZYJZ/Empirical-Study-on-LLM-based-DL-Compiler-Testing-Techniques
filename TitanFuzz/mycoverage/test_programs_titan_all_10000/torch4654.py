import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
torch.Tensor.istft(input_tensor, n_fft=10, hop_length=1, win_length=10, window=None, center=True, normalized=False, onesided=None, length=None, return_complex=False)