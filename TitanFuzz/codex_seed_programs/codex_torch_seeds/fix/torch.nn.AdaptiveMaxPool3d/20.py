'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
input_data = torch.randn(20, 16, 50, 32, 45)
adaptive_max_pool_3d = torch.nn.AdaptiveMaxPool3d(3)
output = adaptive_max_pool_3d(input_data)
print(output)