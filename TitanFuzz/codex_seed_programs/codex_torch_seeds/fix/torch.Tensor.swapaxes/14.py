'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
print('input tensor:', input_tensor)
swapaxes_tensor = input_tensor.swapaxes(0, 2)
print('swapaxes tensor:', swapaxes_tensor)