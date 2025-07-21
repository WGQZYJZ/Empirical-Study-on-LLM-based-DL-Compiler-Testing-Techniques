'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch
input_tensor = torch.randn(1, 1, 5)
print(input_tensor)
output_tensor = torch.nn.functional.adaptive_max_pool1d(input_tensor, 3)
print(output_tensor)