'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 30.0, 45.0, 60.0, 90.0], dtype=torch.float)
output = torch.cos(input_data)
print('Input: {}'.format(input_data))
print('Output: {}'.format(output))