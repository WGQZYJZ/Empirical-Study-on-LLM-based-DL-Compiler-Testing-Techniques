'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfc\ntorch.erfc(input, *, out=None)\n'
import torch
input_data = torch.randn(100)
output_data = torch.erfc(input_data)
print(input_data)
print(output_data)