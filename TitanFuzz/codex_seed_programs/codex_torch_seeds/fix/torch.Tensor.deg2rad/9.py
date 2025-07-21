'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[0.0, 180.0, 360.0], [90.0, 270.0, 450.0]])
print('input tensor:', input_tensor)
output_tensor = input_tensor.deg2rad()
print('output tensor:', output_tensor)