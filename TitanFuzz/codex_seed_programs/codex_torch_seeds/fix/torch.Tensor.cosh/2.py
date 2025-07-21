'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh\ntorch.Tensor.cosh(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
cosh_tensor = input_tensor.cosh()
print('Cosh tensor: ', cosh_tensor)