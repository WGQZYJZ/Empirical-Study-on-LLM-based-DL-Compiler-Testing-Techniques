'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.arange(1, 9, dtype=torch.float64).reshape(1, 2, 2, 2)
print('input is: ', input)
output = torch.fft.ifft(input, norm=None)
print('output is: ', output)
output = torch.fft.ifft(input, norm=None, dim=1)
print('output is: ', output)
output = torch.fft.ifft(input, norm=None, dim=(- 1))
print('output is: ', output)
output = torch.fft.ifft(input, norm=None, dim=2)
print('output is: ', output)