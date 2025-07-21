'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
input_data = torch.tensor(np.random.rand(3, 3), dtype=torch.float32)
print('Input data: \n', input_data)
print('Task 3: Call the API torch.nn.functional.dropout')
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True)
print('Output data: \n', output_data)
print('Is the output the same as the input? ', torch.all(torch.eq(input_data, output_data)))