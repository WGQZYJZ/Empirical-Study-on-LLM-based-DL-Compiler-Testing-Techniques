'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu\ntorch.Tensor.triu(_input_tensor, diagonal=0)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 3)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.triu(diagonal=0)
print('output_tensor: ', output_tensor)