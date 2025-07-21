'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftshift\ntorch.fft.ifftshift(input, dim=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
result = torch.fft.ifftshift(input_data)
print(result)