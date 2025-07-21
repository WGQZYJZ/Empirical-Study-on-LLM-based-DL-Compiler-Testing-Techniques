'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
data = torch.rand(3, 3, 3)
fft_data = torch.fft.rfftn(data)
print(data)
print(fft_data)