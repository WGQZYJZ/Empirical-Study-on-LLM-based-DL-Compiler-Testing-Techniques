'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.all(_input_tensor, dim=None, keepdim=False)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)