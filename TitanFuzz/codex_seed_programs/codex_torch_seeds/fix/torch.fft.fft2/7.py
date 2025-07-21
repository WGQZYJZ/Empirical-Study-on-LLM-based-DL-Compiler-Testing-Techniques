'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 4, 5)
output_data = torch.fft.fft2(input_data, s=None, dim=((- 2), (- 1)), norm=None, out=None)
print('input_data: ', input_data)
print('output_data: ', output_data)