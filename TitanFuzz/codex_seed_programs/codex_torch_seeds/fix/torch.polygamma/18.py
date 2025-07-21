'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input_data = torch.randint(1, 10, (3, 3), dtype=torch.float32)
print('Input data:', input_data)
output = torch.polygamma(1, input_data)
print('Output:', output)