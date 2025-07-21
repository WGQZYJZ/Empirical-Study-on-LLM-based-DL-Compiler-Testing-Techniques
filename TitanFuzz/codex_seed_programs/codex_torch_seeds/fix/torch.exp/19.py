'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
input_tensor = torch.randn(1, 3)
print(input_tensor)
output_tensor = torch.exp(input_tensor)
print(output_tensor)