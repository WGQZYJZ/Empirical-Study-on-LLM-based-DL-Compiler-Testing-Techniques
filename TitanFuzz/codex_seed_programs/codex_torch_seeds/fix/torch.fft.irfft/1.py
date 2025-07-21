'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
from torch.autograd import Variable
import numpy as np
input = np.random.randn(1, 3, 4, 4)
input = Variable(torch.from_numpy(input))
output = torch.fft.irfft(input, 3, 2)
print(output)