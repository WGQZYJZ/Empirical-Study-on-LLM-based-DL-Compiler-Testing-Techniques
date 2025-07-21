'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_data = torch.rand(1, 1, 3, 3)
output = torch.Tensor.deg2rad(input_data)
print('The result of deg2rad is: ', output)