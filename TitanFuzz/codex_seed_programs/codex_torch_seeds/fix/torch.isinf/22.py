'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input_data = torch.Tensor([float('inf'), float('-inf'), float('nan'), 1, 2, 3])
output_data = torch.isinf(input_data)
print('input_data:', input_data)
print('output_data:', output_data)