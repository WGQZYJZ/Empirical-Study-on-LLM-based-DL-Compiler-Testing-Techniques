'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import torch.nn as nn
input_tensor = torch.randn(1, 3, 224, 224)
gelu = nn.GELU()
output = gelu(input_tensor)
print(output)