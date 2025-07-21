'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft\ntorch.fft.fft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(1, 4, 4)
print(x)
y = torch.fft.fft(x)
print(y)
x_np = x.numpy()
y_np = y.numpy()
x_np_fft = np.fft.fft(x_np)
print(x_np_fft)
print(y_np)
x_np = x.numpy()
y_np = y.numpy()
x_np_fft = np.fft.fft(x_np)
print(x_np_fft)
print(y_np)