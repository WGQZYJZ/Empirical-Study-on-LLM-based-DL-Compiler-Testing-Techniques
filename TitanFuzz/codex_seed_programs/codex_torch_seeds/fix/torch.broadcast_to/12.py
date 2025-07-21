'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2], [3, 4]])
shape = (2, 2, 2)
output_tensor = torch.broadcast_to(input_tensor, shape)
print('Output tensor: ', output_tensor)