'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
input = torch.randn(1, 1, 6, 6, 6)
output = torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))(input)
print(output)