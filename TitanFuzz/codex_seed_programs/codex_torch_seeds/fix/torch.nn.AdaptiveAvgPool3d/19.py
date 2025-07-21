'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
input = torch.randn(1, 3, 5, 5, 5)
output = torch.nn.AdaptiveAvgPool3d(output_size=3)(input)
print(output)