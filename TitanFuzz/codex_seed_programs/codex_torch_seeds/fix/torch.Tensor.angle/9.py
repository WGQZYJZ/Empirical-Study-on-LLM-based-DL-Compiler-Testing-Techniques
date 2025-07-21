'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data: ', input_data)
angle = input_data.angle()
print('angle: ', angle)