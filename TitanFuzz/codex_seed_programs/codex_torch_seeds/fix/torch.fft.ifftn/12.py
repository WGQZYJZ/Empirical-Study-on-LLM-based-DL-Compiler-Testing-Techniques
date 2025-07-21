'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifftn\ntorch.fft.ifftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3, 4, 5)
print('Input data: ', input_data)
output_data = torch.fft.ifftn(input_data)
print('Output data: ', output_data)