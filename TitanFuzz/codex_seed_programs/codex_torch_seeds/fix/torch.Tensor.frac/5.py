'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor : ', input_tensor)
print('frac : ', input_tensor.frac())