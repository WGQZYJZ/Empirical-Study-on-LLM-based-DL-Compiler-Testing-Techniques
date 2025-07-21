'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
input_data = torch.randn(5, 3)
selu_layer = torch.nn.SELU(inplace=False)
output = selu_layer(input_data)
print(output)