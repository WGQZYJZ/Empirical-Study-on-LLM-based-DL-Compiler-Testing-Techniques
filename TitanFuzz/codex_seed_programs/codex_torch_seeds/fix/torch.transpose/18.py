'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.transpose(input_data, 0, 1)
print(output_data)