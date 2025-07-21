'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftshift\ntorch.fft.ifftshift(input, dim=None)\n'
import torch
input_data = torch.arange(1, 17).view(4, 4)
print(input_data)
output_data = torch.fft.ifftshift(input_data)
print(output_data)