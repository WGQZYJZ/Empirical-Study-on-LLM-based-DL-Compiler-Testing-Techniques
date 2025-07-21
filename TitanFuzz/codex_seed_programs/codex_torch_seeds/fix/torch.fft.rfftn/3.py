'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input = torch.randn(1, 1, 16, 16)
output = torch.fft.rfftn(input)
print(output)
print(output.shape)