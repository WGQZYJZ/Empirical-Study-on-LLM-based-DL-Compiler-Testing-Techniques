'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
angle_tensor = torch.Tensor.angle(input_tensor)
print(angle_tensor)