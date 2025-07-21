'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftshift\ntorch.fft.ifftshift(input, dim=None)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
output = torch.fft.ifftshift(input)
print(output)
output = torch.fft.ifftshift(input, dim=0)
print(output)
output = torch.fft.ifftshift(input, dim=1)
print(output)
output = torch.fft.ifftshift(input, dim=2)
print(output)