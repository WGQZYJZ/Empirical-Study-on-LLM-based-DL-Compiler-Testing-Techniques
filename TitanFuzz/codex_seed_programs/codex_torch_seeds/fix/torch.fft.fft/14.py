'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft\ntorch.fft.fft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(4, 3, 2)
output = torch.fft.fft(input)
print(output)
output = torch.fft.ifft(input)
print(output)
input = torch.randn(3, 3)
output = torch.fft.fft2(input)
print(output)
input = torch.randn(3, 3)
output = torch.fft.ifft2(input)
print(output)
input = torch.randn(3, 3)
output = torch.fft.fftn(input)
print(output)
input = torch.randn(3, 3)