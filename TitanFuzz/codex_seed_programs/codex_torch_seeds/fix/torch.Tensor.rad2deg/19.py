'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
output_tensor = torch.Tensor.rad2deg(input_tensor)
print(output_tensor)