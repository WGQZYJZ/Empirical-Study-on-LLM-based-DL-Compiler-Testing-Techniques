'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
angle_tensor = input_tensor.angle()
print('input_tensor:', input_tensor)
print('angle_tensor:', angle_tensor)