'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_shared\ntorch.Tensor.is_shared(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.is_shared(_input_tensor)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)