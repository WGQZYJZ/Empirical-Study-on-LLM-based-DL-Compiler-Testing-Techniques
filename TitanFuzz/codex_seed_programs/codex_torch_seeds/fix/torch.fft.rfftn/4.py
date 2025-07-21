'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
input_data = torch.rand(10, 10, 10)
torch.fft.rfftn(input_data)
torch.fft.irfftn(input_data)