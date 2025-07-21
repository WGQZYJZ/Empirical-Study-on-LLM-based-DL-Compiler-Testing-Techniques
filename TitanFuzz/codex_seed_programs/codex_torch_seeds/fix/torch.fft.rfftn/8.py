'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
from torch import fft
from torch.nn.functional import pad
input = torch.randn(2, 3, 4, 5)
fft_output = fft.rfftn(input, dim=(- 1))
fft_output = fft.rfftn(input, dim=2)
fft_output = fft.rfftn(input, dim=(2, 3))
fft_output = fft.rfftn(pad(input, (0, 0, 0, 0, 0, 2), mode='constant'), dim=(- 1))
fft_output = fft.rfftn(pad(input, (0, 0, 0, 0, 2, 3), mode='constant'), dim=(- 1))