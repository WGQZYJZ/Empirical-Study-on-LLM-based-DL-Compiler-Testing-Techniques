'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.arange(12, dtype=torch.float32).reshape(3, 4)
print('Input data: \n', input_data)
output_data = torch.amin(input_data, 1, False)
print('Output data: \n', output_data)