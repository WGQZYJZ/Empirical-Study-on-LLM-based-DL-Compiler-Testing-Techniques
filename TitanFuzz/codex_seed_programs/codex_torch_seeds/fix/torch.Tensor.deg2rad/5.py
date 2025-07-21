'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
output_tensor = torch.Tensor.deg2rad(input_tensor)
print(output_tensor)