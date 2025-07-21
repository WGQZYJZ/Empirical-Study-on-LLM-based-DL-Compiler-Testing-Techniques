'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_tensor = torch.tensor([0.0, 30.0, 45.0, 60.0, 90.0])
output_tensor = torch.Tensor.deg2rad(input_tensor)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)