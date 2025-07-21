'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
input_data = np.random.randn(3, 4, 5)
input_data = torch.from_numpy(input_data)
output_data = torch.fft.rfftn(input_data, 3, 0)
print(output_data)