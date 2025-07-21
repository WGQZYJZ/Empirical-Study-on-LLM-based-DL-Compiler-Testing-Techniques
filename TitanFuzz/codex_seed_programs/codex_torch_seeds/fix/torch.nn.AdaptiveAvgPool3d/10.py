'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(20, 16, 50, 32, 45)
output = nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))(input)
print(output.shape)