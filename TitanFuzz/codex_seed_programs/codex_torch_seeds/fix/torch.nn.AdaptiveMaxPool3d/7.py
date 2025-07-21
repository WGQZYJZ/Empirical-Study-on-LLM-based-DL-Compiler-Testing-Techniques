'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch
input = torch.randn(1, 1, 10, 10, 10)
output = torch.nn.AdaptiveMaxPool3d((1, 1, 1))(input)
print(output.size())
(output, indices) = torch.nn.AdaptiveMaxPool3d((1, 1, 1), return_indices=True)(input)
print(output.size(), indices.size())