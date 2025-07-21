'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_data = torch.clone(input_data)
print(output_data)