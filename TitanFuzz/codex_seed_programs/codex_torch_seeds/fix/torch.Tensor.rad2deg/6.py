'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
output_tensor = input_tensor.rad2deg()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)