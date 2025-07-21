'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool1d\ntorch.nn.functional.max_pool1d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import numpy as np
input_size = (1, 1, 4)
input_data = np.array([[1, 2, 3, 4]], dtype=np.float32)
input_data = torch.from_numpy(input_data)
input_data = input_data.view(input_size)
print('input_data = \n{}'.format(input_data))
output = torch.nn.functional.max_pool1d(input_data, kernel_size=2)
print('output = \n{}'.format(output))