'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
in_data = np.random.randn(2, 3, 4, 5)
in_data = torch.tensor(in_data, dtype=torch.float32)
out_data = torch.fft.fft2(in_data)
print(out_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
in_data = np.random.randn(2, 3, 4, 5)
in_data = torch.tensor(in_data, dtype=torch.float32)
out_data = torch.fft.fftn(in_data)
print(out_data)