'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft\ntorch.fft.fft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
in_data = np.random.randn(4, 3, 2)
in_tensor = torch.tensor(in_data)
out_tensor = torch.fft.fft(in_tensor)
print('in_tensor: {}'.format(in_tensor))
print('out_tensor: {}'.format(out_tensor))