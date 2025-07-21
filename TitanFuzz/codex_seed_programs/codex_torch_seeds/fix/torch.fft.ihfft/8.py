'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ihfft\ntorch.fft.ihfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)
print(input_data)
output_data = torch.fft.ihfft(input_data, n=None, dim=(- 1), norm=None, out=None)
print(output_data)