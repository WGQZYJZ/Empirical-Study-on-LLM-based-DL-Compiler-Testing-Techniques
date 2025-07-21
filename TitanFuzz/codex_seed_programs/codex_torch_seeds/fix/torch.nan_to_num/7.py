'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
input_data[0] = float('nan')
input_data[1] = float('-inf')
input_data[2] = float('inf')
print(input_data)
output = torch.nan_to_num(input_data)
print(output)