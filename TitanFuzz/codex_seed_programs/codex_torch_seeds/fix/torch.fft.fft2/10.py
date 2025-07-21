'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(2, 3, 4)
output = torch.fft.fft2(input, s=None, dim=((- 2), (- 1)), norm=None, out=None)
print(input)
print(output)
input_np = input.numpy()
output_np = np.fft.fft2(input_np)
print(output_np)