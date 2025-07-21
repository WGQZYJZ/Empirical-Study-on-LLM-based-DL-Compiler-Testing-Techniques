'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh\ntorch.Tensor.arccosh(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
arccosh_tensor = input_tensor.arccosh()
print('input_tensor: \n', input_tensor)
print('arccosh_tensor: \n', arccosh_tensor)