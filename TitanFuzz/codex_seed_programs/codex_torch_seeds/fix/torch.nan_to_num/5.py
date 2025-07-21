'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
input = torch.tensor([[1, float('nan')], [float('inf'), float('-inf')]])
print(input)
output = torch.nan_to_num(input)
print(output)