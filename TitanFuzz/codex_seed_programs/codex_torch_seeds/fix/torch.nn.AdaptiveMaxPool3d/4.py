'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(10, 10, 10, 10, 10)
pool = nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))
output = pool(input)
print(output.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(10, 10, 10, 10, 10)