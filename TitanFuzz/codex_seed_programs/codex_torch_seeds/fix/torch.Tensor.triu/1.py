'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu\ntorch.Tensor.triu(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(5, 5)
print('input_tensor: ', input_tensor)
input_tensor_triu = torch.Tensor.triu(input_tensor, diagonal=0)
print('input_tensor_triu: ', input_tensor_triu)