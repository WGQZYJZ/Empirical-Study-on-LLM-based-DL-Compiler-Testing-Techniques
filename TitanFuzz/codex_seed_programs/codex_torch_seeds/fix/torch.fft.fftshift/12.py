'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
input_data = torch.randn(1, 1, 4, 4)
print('Input data: ', input_data)
output_data = torch.fft.fftshift(input_data)
print('Output data: ', output_data)