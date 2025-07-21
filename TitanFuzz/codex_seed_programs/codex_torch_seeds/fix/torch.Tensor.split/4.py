'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
input_tensor = torch.randn(16, 4, 4)
print(input_tensor)
output_tensor = input_tensor.split(split_size=4, dim=0)
print(output_tensor)