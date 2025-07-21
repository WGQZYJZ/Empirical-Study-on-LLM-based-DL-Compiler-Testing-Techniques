'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
input_data = torch.arange(20, dtype=torch.float32).reshape(4, 5)
result = torch.clip(input_data, min=5, max=15)
print('Input data:\n', input_data)
print('Result:\n', result)