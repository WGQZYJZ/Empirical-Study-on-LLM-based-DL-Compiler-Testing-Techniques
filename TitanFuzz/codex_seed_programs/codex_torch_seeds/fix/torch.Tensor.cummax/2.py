'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: \n', input_tensor)
cummax_tensor = input_tensor.cummax(dim=1)
print('Cummax tensor: \n', cummax_tensor)