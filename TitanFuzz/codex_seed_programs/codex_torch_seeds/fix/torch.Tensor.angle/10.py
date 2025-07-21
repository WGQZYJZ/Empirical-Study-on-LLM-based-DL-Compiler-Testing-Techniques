'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(1, 3)
angle_tensor = torch.Tensor.angle(input_tensor)
print('Input tensor:')
print(input_tensor)
print('Angle tensor:')
print(angle_tensor)