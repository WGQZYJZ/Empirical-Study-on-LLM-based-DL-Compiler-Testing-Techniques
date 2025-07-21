'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu\ntorch.Tensor.triu(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.rand(3, 3)
triu_tensor = input_tensor.triu()
print('input_tensor: ', input_tensor)
print('triu_tensor: ', triu_tensor)