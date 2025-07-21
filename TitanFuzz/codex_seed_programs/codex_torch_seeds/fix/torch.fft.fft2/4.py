'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input_data = np.random.randn(2, 3, 4, 5)
input_data = torch.tensor(input_data)
output = torch.fft.fft2(input_data)
print(output)
output = torch.fft.ifft2(input_data)
print(output)
output = torch.fft.rfft2(input_data)
print(output)
output = torch.fft.irfft2(input_data)
print(output)