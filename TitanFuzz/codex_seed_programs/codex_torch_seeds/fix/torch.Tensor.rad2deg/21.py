'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
rad2deg_tensor = input_tensor.rad2deg()
print('The original tensor: ', input_tensor)
print('The converted tensor: ', rad2deg_tensor)