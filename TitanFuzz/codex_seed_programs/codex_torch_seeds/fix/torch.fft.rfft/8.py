'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input_data = torch.rand(1, 2, 3, 4)
output_data = torch.fft.rfft(input_data)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, signal_ndim=1, normalized=False, onesided=True, *, out=None)\n'
import torch
input_data = torch.rand(1, 2, 3, 4)
output_data = torch.fft.rfft2(input_data)
print(output_data)