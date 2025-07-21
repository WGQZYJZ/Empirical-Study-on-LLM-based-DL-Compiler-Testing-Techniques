'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
import torch
input = torch.randn(1, 3, 10)
output = torch.nn.AdaptiveMaxPool1d(3)(input)
print(output)