'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
import torch.nn.functional as F
import numpy as np
print('Task 1: import PyTorch')
print(torch.__version__)
print('')
print('Task 2: Generate input data')
input_data = np.random.rand(1, 2, 3, 4, 5)
input_tensor = torch.tensor(input_data)
print(input_tensor.shape)
print('')
print('Task 3: Call the API torch.nn.functional.adaptive_avg_pool3d')
output_size = (2, 3, 4)
out = F.adaptive_avg_pool3d(input_tensor, output_size)
print(out.shape)