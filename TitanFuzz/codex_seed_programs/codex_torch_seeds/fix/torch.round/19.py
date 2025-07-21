'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.1, 2.2, 3.3, 4.4], dtype=torch.float32)
output_data = torch.round(input_data)
print('input_data:', input_data)
print('output_data:', output_data)