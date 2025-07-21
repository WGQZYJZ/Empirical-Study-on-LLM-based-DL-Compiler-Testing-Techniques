'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ihfft\ntorch.fft.ihfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print(input_data)
output = torch.fft.ihfft(input_data)
print(output)