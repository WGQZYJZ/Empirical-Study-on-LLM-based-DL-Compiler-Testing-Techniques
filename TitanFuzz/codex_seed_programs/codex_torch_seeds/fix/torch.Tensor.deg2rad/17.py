'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_data = torch.Tensor([0, 30, 45, 60, 90])
radians = torch.Tensor.deg2rad(input_data)
print('Degrees: ', input_data)
print('Radians: ', radians)