'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor\ntorch.Tensor.floor(_input_tensor)\n'
import torch
input_tensor = torch.randn((1, 3, 3, 3))
output_tensor = torch.Tensor.floor(input_tensor)
print('input_tensor: \n', input_tensor)
print('output_tensor: \n', output_tensor)