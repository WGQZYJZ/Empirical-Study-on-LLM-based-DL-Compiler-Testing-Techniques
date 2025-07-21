'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
input_data = torch.rand(1, 1, 3, 3)
print('Input data is: ', input_data)
result = torch.exp2(input_data)
print('Result is: ', result)