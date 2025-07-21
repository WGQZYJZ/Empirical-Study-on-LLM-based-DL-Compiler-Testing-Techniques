'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = input_tensor.mul(2)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\nExpected output:\ninput_tensor: tensor([[1, 2, 3],\n        [4, 5, 6]])\noutput_tensor: tensor([[ 2,  4,  6],\n        [ 8, 10, 12]])\n'