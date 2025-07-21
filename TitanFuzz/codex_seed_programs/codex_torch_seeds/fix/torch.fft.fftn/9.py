'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
import time
from torch.autograd import gradcheck
input = np.random.randint(low=0, high=100, size=(2, 3, 4, 5, 6, 7))
input = torch.from_numpy(input)
print('input:', input)
out = torch.fft.fftn(input)
print('out:', out)