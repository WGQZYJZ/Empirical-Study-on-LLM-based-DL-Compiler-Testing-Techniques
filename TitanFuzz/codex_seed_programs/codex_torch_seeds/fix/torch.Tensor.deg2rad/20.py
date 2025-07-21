'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_tensor = torch.tensor([0, 30, 45, 60, 90])
input_tensor_rad = input_tensor.deg2rad()
print('input_tensor: ', input_tensor)
print('input_tensor_rad: ', input_tensor_rad)