'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft\ntorch.fft.fft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
x = torch.rand(4, 2, 8)
print(x)
y = torch.fft.fft(x, 2, 1)
print(y)
x_np = x.numpy()
y_np = np.fft.fft(x_np, 2, 1)
print(y_np)
print(np.allclose(y.numpy(), y_np))