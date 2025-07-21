'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input = torch.randn(4, 4, 8)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)
print(output)