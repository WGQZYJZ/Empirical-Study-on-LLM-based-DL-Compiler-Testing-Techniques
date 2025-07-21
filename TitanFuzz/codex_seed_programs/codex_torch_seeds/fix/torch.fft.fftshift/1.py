'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
import numpy as np
x = torch.randn(4, 4, 4)
print('x:', x)
y = torch.fft.fftshift(x, dim=0)
print('y:', y)
a = np.fft.fftshift(x.numpy(), axes=0)
print('a:', a)
print('x == y:', torch.allclose(x, y))
print('x == a:', np.allclose(x.numpy(), a))