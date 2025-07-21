'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 4, 5)
result = torch.fft.ifft(input_data, n=None, dim=(- 1), norm=None, out=None)
print('result: ', result)