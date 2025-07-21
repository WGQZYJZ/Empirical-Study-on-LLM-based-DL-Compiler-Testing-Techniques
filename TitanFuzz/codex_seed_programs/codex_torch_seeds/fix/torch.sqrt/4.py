'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
input_data = torch.randn(10, 20)
print(input_data)
output = torch.sqrt(input_data)
print(output)