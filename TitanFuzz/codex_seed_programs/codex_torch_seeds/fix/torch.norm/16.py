"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
input_data = torch.randn(3, 4)
output_data = torch.norm(input_data, p=2, dim=1)
print('input_data:')
print(input_data)
print('output_data:')
print(output_data)