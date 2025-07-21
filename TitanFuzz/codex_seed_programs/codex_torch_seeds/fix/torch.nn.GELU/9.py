'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
input_data = torch.randn(10, 10)
gelu_layer = torch.nn.GELU()
output = gelu_layer(input_data)
print(output)