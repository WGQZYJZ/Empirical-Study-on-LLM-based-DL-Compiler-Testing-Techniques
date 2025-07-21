'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftfreq\ntorch.fft.fftfreq(n, d=1.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import torch
input_data = torch.randn(4, 4)
output = torch.fft.fftfreq(input_data.shape[(- 1)], d=1.0)
print('input_data: ', input_data)
print('output: ', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, signal_ndim, normalized=False, onesided=True, *, out=None, signal_sizes=None, signal_axes=None)\n'
import torch
import torch
input_data = torch.randn(4, 4)