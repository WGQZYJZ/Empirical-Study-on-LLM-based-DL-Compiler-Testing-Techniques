'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.block_diag')
input_data = [torch.arange(1, 7).reshape(2, 3), torch.arange(7, 13).reshape(2, 3)]
output_data = torch.block_diag(*input_data)
print('input data: ', input_data)
print('output data: ', output_data)