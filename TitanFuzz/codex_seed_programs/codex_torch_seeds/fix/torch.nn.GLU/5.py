'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
from torch import nn
input_data = torch.randn(1, 2, 3, 4)
glu = nn.GLU(dim=(- 1))
output = glu(input_data)
print(output)