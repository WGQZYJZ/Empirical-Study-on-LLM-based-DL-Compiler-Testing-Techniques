'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([1.1, 2.2, 3.3])
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.rad2deg()
print('Output tensor: ', output_tensor)