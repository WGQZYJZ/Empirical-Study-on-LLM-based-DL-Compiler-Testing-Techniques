'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
input = torch.arange(0, 8).reshape(1, 2, 2, 2)
print('Input: ', input)
output = torch.fft.rfftn(input, s=None, dim=None, norm=None, out=None)
print('Output: ', output)