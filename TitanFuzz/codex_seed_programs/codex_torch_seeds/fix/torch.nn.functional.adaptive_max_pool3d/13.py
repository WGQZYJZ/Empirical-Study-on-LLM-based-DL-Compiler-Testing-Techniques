'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 32, 32, 32)
output_data = torch.nn.functional.adaptive_max_pool3d(input_data, (1, 1, 1))
print(output_data)