'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float)
output_data = torch.nn.LogSoftmax(dim=1)(input_data)
print('Input:')
print(input_data)
print('Output:')
print(output_data)
print('\nCalculate the result by hand:')
print('Input:')
print(input_data)
print('Output:')
print(torch.log(torch.softmax(input_data, dim=1)))
print('\nUse the API torch.nn.functional.log_softmax')
print('Input:')
print(input_data)