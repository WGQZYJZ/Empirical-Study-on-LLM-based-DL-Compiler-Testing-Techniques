'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
input_data = torch.randn(1, 1, 4, 4)
print(input_data)
print(torch.fft.fft2(input_data))
print(torch.fft.fft2(input_data, s=None, dim=((- 2), (- 1)), norm=None, out=None))