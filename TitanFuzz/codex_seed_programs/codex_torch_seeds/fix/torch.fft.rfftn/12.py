'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
x = torch.rand(4, 4, 4)
print(x)
y = torch.fft.rfftn(x)
print(y)
x_np = x.numpy()
y_np = y.numpy()
y_np_verify = np.fft.rfftn(x_np)
print(y_np)
print(y_np_verify)
print(np.allclose(y_np, y_np_verify))