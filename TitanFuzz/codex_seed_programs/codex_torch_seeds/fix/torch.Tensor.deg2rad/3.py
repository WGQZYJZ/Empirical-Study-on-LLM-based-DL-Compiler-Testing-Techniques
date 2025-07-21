'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_tensor = torch.tensor([0, 30, 45, 60, 90])
radian_tensor = input_tensor.deg2rad()
print(radian_tensor)
print(radian_tensor)