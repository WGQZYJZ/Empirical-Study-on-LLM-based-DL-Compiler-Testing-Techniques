'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
from torch.nn import GELU
input_data = torch.randn(1, 3)
output = GELU()(input_data)
print(output)