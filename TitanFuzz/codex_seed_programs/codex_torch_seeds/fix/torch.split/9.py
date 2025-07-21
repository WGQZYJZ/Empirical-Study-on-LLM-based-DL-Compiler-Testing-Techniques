'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
output_tensor = torch.split(input_tensor, 2, dim=0)
print(output_tensor)
output_tensor = torch.split(input_tensor, 2, dim=1)
print(output_tensor)
output_tensor = torch.split(input_tensor, [1, 2, 1], dim=0)
print(output_tensor)
output_tensor = torch.split(input_tensor, [1, 2, 1], dim=1)
print(output_tensor)