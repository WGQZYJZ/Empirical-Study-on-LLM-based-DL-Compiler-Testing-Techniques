'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(20, 16, 50, 32)
output_data = nn.AdaptiveAvgPool2d(output_size=5)(input_data)
print(output_data.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(20, 16, 50, 32)