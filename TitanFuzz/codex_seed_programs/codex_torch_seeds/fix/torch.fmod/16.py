'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
input_data = torch.randint(10, (3, 3), dtype=torch.float)
print('Input data: ', input_data)
result_data = torch.fmod(input_data, 2)
print('Result data: ', result_data)