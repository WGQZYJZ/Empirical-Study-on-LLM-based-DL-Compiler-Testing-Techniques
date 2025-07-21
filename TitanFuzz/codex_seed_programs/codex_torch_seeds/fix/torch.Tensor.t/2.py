'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 5)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.t()
print('output_tensor: ', output_tensor)