'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool1d\ntorch.nn.MaxUnpool1d(kernel_size, stride=None, padding=0)\n'
import torch
import torch.nn as nn
input_size = (1, 1, 4)
input_data = torch.randint(low=0, high=9, size=input_size, dtype=torch.float)
print('Input data: ', input_data)
max_pool = nn.MaxPool1d(kernel_size=2, stride=2, return_indices=True)
(output, indices) = max_pool(input_data)
print('Output: ', output)
print('Indices: ', indices)
max_unpool = nn.MaxUnpool1d(kernel_size=2, stride=2)
unpool_output = max_unpool(output, indices, output_size=input_size)
print('Unpool output: ', unpool_output)