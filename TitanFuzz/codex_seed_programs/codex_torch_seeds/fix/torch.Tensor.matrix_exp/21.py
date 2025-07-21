'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_exp\ntorch.Tensor.matrix_exp(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 2)
output_tensor = input_tensor.matrix_exp()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)