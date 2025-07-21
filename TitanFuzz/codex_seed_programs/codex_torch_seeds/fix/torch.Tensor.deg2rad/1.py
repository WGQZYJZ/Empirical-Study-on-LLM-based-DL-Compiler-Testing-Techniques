'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([[0, 30, 45, 60, 90]], dtype=torch.float)
output_tensor = torch.Tensor.deg2rad(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)