'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: ', _input_tensor)
torch.Tensor.fill_(_input_tensor, value=2)
print('Output tensor: ', _input_tensor)