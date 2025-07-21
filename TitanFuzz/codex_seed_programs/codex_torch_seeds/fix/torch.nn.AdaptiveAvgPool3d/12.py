'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
input = torch.randn(1, 4, 6, 6, 6)
print(input)
output = torch.nn.AdaptiveAvgPool3d((2, 2, 2))(input)
print(output)