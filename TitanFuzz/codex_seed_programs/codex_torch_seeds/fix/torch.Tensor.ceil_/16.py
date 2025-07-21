'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil_\ntorch.Tensor.ceil_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
torch.Tensor.ceil_(input_tensor)
print('Output tensor: ', input_tensor)