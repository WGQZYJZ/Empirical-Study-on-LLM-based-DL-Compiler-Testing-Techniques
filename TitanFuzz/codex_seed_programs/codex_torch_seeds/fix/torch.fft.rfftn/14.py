'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
from torch import fft
input_data = torch.randn(16, 4, 4)
print('Input data: ', input_data)
output = fft.rfftn(input_data, 2, 2)
print('Output: ', output)
print('Output size: ', output.size())