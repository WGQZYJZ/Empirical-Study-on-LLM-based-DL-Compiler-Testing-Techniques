'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
output_data = torch.acosh(input_data)
print(output_data)