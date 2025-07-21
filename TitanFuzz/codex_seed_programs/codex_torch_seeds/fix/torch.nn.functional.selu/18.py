'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
input_data = torch.randn(1, 2, 3)
print(input_data)
output_data = torch.nn.functional.selu(input_data)
print(output_data)