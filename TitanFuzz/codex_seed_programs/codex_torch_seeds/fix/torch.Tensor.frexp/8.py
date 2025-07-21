'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frexp\ntorch.Tensor.frexp(_input_tensor, input)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
frexp_tensor = input_tensor.frexp()
print('Input tensor: ', input_tensor)
print('Frexp tensor: ', frexp_tensor)