'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
input_data = torch.rand(1, 1, 6)
print(input_data)
m = torch.nn.AdaptiveMaxPool1d(3)
output = m(input_data)
print(output)