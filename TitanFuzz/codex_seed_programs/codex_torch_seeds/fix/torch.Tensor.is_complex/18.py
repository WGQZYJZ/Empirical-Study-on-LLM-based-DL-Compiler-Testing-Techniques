'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
output = input_tensor.is_complex()
print('input tensor: ', input_tensor)
print('output: ', output)