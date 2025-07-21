'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
input = torch.randn(1, 1, 9, 9)
output = torch.nn.AdaptiveMaxPool2d((3, 3))(input)
print(output)