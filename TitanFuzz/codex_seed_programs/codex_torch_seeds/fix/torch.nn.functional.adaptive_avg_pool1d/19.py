'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
input = torch.randn(1, 2, 5)
output = torch.nn.functional.adaptive_avg_pool1d(input, 2)
print(output)