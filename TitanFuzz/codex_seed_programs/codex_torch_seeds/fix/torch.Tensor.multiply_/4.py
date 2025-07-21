'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
input_tensor = torch.arange(1, 6)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.multiply_(input_tensor, 2)
print('output_tensor: ', output_tensor)
'\ntorch.Tensor.multiply_\ntorch.Tensor.mul_\ntorch.Tensor.divide_\ntorch.Tensor.div_\ntorch.Tensor.add_\ntorch.Tensor.sub_\n'