'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
input_data = torch.randn(1, 1, 7)
print('Input data:', input_data)
output_data = torch.nn.AdaptiveMaxPool1d(3)(input_data)
print('Output data:', output_data)