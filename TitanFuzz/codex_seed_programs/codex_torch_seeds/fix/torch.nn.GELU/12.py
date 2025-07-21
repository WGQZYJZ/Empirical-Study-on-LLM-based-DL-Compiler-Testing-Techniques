'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
input_data = torch.randn(2, 3)
x = torch.nn.GELU()(input_data)
print(x)