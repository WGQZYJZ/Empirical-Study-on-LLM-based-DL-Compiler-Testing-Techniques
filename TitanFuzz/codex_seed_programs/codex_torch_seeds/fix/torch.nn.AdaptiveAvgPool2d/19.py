'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch.nn as nn
input_tensor = torch.randn(1, 1, 4, 4)
avg_pooling_layer = nn.AdaptiveAvgPool2d(output_size=2)
output = avg_pooling_layer(input_tensor)
print(output)