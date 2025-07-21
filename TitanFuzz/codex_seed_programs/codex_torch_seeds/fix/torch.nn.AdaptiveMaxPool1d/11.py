'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
input_data = torch.randint(1, 10, (3, 3, 4), dtype=torch.float32)
print('Input data: ', input_data)
output_size = 2
output_data = torch.nn.AdaptiveMaxPool1d(output_size)(input_data)
print('Output data: ', output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
input_data = torch.randint(1, 10, (3, 3, 4, 4), dtype=torch.float32)
print('Input data: ', input_data)