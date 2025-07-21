'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
input_data = torch.tensor([[4, 9, 16, 25]])
result = torch.sqrt(input_data)
print('Input data: {}'.format(input_data))
print('Result: {}'.format(result))