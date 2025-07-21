'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
import numpy as np
from torch.nn import ZeroPad2d
input_data = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], dtype=np.float32)
input_tensor = torch.from_numpy(input_data)
padding = (1, 1)
zero_pad = ZeroPad2d(padding)
output_tensor = zero_pad(input_tensor)
print('Input tensor:')
print(input_tensor)
print('Output tensor:')
print(output_tensor)