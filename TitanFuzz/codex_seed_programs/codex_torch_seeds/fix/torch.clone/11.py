'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(2, 3)
output = torch.clone(input_data)
print(output)
input_data = torch.randn(2, 3, 4)
output = torch.clone(input_data)
print(output)