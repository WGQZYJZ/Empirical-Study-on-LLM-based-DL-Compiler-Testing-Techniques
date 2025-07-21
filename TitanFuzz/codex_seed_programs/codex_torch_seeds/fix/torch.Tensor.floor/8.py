'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor\ntorch.Tensor.floor(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.floor(input_tensor)
print('output_tensor: ', output_tensor)