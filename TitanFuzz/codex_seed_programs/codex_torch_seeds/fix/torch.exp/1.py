'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.exp(input_data)
print(output_data)