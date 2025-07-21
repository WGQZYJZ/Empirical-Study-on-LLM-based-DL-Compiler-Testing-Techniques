'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
data = torch.arange(0, 9).view(1, 1, 9).float()
print('Input data: ', data)
adaptive_max_pool_1d = torch.nn.AdaptiveMaxPool1d(3)
output = adaptive_max_pool_1d(data)
print('Output: ', output)