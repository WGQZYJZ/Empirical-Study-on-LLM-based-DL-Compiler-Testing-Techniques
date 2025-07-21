'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
input_data = torch.randn(10)
print(input_data)
output_data = torch.nn.SELU(inplace=False)(input_data)
print(output_data)