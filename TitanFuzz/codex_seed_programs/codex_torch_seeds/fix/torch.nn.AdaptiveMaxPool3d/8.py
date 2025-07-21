'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch
input = torch.randn(20, 16, 50, 32, 45)
output = torch.nn.AdaptiveMaxPool3d(output_size=(5, 4, 3))(input)
print(output.size())