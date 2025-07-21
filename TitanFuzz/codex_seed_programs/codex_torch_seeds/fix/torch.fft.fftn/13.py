'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
import time
input = torch.randn(1, 2, 3, 4)
start = time.time()
output = torch.fft.fftn(input)
end = time.time()
print('input size: ', input.size())
print('output size: ', output.size())
print('time: ', (end - start))