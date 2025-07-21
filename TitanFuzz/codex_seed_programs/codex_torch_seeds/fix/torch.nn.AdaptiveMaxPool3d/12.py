'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 3, 4, 4, 4)
output = nn.AdaptiveMaxPool3d(output_size=(1, 2, 2))(input)
print(output)