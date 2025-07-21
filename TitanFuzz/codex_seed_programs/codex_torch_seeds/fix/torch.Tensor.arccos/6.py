'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.arccos(input_tensor)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)