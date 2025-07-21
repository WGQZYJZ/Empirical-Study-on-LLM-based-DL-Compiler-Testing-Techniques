'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.matmul(input_tensor, input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\ntorch.Tensor.matmul(_input_tensor, tensor2)\ninput_tensor: tensor([[1, 2, 3],\n        [4, 5, 6]])\noutput_tensor: tensor([[14, 32, 50],\n        [32, 77, 122]])\n'