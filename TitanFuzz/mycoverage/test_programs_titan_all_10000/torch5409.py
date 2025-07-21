import torch
from torch import nn
from torch.autograd import Variable
input = np.random.randn(1, 3, 4, 4)
input = Variable(torch.from_numpy(input))
output = torch.fft.irfft(input, 3, 2)