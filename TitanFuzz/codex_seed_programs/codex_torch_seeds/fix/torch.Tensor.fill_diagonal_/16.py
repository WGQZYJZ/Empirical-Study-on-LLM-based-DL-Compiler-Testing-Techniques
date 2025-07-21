'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
torch.Tensor.fill_diagonal_(input_tensor, 1, wrap=True)
print('Output tensor: ', input_tensor)