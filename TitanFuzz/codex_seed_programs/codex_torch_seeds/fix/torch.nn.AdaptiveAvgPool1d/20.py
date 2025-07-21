'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
import numpy as np
input_size = (1, 1, 4)
input_data = torch.tensor(np.arange(1, 5, dtype=np.float32).reshape(input_size))
print('Input: ', input_data)
avg_pool_1d = torch.nn.AdaptiveAvgPool1d(output_size=2)
output = avg_pool_1d(input_data)
print('Output: ', output)