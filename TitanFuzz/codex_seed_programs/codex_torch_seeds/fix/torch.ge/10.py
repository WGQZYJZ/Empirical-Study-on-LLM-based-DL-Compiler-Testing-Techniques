'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.ge(input_data, 0)
print(output_data)