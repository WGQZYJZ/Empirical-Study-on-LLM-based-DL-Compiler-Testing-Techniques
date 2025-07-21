'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: ', _input_tensor)
_output_tensor = _input_tensor.all(dim=0, keepdim=True)
print('Output tensor: ', _output_tensor)