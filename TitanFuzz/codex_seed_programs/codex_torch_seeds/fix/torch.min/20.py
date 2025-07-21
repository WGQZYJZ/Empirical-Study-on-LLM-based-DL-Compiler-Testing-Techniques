'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = torch.min(input_tensor, dim=0, keepdim=False)
print(output_tensor)
print(output_tensor[0])
print(output_tensor[1])