'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input_data = torch.rand(1, 3, 1, 1)
broadcast_data = torch.broadcast_to(input_data, (3, 3, 3, 3))
print('Input data: ', input_data)
print('Broadcast data: ', broadcast_data)