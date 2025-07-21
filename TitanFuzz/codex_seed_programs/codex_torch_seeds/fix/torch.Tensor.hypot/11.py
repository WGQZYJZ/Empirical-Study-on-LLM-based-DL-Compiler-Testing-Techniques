'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot\ntorch.Tensor.hypot(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
print('The input tensor: ', input_tensor)
print('The output tensor: ', input_tensor.hypot(input_tensor))