'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randint(0, 10, (5, 5))
print(input_data)
print('Task 3: Call the API torch.tril')
output = torch.tril(input_data, diagonal=0)
print(output)