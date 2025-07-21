'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(1, 3, 4, 5)
print('Input: ', input)
out = torch.fft.fftn(input, s=None, dim=None, norm=None, out=None)
print('Output: ', out)
print('Output type: ', type(out))
print('Output shape: ', out.shape)
print('Output size: ', out.size())
print('Output dtype: ', out.dtype)
out_np = out.numpy()
print('Output numpy: ', out_np)
print('Output numpy type: ', type(out_np))