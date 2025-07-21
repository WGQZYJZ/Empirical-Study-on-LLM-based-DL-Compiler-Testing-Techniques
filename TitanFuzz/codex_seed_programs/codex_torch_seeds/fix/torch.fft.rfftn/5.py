'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import torch
input_data = torch.rand(2, 3, 4)
output_data = torch.fft.rfftn(input_data, s=(4,), dim=2, norm=None, out=None)
print(output_data)