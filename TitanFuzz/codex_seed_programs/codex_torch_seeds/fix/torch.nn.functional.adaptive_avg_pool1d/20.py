'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
input = torch.randn(1, 1, 3)
output_size = (2,)
output = torch.nn.functional.adaptive_avg_pool1d(input, output_size)
print(output)