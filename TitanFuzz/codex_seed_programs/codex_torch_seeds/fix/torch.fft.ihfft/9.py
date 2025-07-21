'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ihfft\ntorch.fft.ihfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(3, 8, 5, dtype=torch.float)
print(input)
output = torch.fft.ihfft(input, n=None, dim=(- 1), norm=None, out=None)
print(output)