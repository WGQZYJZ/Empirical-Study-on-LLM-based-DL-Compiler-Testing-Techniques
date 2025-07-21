'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round_\ntorch.Tensor.round_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: \n', input_tensor)
torch.Tensor.round_(input_tensor)
print('Output tensor: \n', input_tensor)