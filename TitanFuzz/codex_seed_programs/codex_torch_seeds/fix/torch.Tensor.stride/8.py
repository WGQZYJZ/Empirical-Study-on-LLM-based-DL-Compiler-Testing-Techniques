'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 2, 2)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', input_tensor.stride())