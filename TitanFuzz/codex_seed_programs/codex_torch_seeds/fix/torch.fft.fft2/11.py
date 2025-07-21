'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.fft
import numpy as np
import torch
input_data = torch.rand(1, 2, 4, 4)
output_data = torch.fft.fft2(input_data)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import torch.fft
import numpy as np
import torch
input_data = torch.rand(1, 2, 4, 4)
output_data = torch.fft.fftn(input_data)
print