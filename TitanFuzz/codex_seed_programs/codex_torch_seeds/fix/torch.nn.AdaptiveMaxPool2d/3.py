'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
input = torch.randn(1, 1, 4, 4)
pool = torch.nn.AdaptiveMaxPool2d(output_size=(2, 2))
output = pool(input)
print(input)
print(output)