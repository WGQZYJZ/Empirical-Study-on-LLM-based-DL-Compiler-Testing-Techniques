'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
import time
import torch
input_tensor = torch.randn(4, 4, 4, 4)
start = time.time()
output_tensor = torch.fft.irfftn(input_tensor, s=None, dim=None, norm=None, out=None)
end = time.time()
print('Time taken: ', (end - start))
print('Output tensor:\n', output_tensor)