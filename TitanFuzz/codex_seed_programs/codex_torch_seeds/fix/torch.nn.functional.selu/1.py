'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(5)
print(input_data)
output_data = F.selu(input_data)
print(output_data)