'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: ', _input_tensor)
_output_tensor = _input_tensor.cholesky()
print('Output tensor: ', _output_tensor)