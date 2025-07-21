'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=0)
print('Cummax tensor: ', cummax_tensor)