'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)
output_data = torch.fft.rfftn(input_data, s=None, dim=None, norm=None, out=None)
print(input_data)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)