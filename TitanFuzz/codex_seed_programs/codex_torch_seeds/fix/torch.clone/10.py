'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
output_data = torch.clone(input_data)
print(output_data)