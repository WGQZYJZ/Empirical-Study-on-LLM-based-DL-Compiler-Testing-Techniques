'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square_\ntorch.Tensor.square_(_input_tensor)\n'
import torch
input_tensor = torch.randn((2, 3))
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.square_(input_tensor)
print('output_tensor: ', output_tensor)
'\nTask 4: Call the API torch.Tensor.add_\ntorch.Tensor.add_(input_tensor, 1)\n'
input_tensor = torch.randn((2, 3))
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.add_(input_tensor, 1)
print('output_tensor: ', output_tensor)
'\nTask 5: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(input_tensor, 2)\n'
input_tensor = torch.randn((2, 3))
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.mul_(input_tensor, 2)