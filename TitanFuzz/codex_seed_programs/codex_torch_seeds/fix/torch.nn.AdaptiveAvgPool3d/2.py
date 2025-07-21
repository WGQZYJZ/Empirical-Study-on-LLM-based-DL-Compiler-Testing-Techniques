'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.nn import AdaptiveAvgPool3d
import torch
from torch.nn import AdaptiveAvgPool3d
input = torch.randn(1, 2, 4, 4, 4)
output = AdaptiveAvgPool3d(output_size=(2, 2, 2))(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size)\n'
import torch
from torch.nn import AdaptiveMaxPool3d
import torch
from torch.nn import AdaptiveMaxPool3d
input = torch.randn(1, 2, 4, 4, 4)