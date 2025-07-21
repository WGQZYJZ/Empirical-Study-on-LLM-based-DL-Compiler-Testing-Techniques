'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4, 5, 6)
output = torch.fft.ifft(input)
print(output.shape)
output = torch.fft.ifft(input, n=2)
print(output.shape)
output = torch.fft.ifft(input, dim=1)
print(output.shape)
output = torch.fft.ifft(input, norm='ortho')
print(output.shape)
output = torch.zeros(3, 4, 5, 6, dtype=torch.complex64)