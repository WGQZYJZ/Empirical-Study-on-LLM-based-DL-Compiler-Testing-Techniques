'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.nn import AdaptiveAvgPool3d
input_data = torch.randn(20, 16, 50, 32, 45)
output_data = AdaptiveAvgPool3d(output_size=(5, 4, 3))(input_data)
print(output_data.shape)