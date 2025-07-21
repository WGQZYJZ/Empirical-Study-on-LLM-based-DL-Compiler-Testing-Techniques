'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
input = torch.randn(1, 3, 10, 10)
output = torch.nn.functional.adaptive_avg_pool2d(input, output_size=(2, 2))
print(output)