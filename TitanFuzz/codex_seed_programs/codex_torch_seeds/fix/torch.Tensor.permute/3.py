'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
_input_tensor = torch.randn(2, 3, 5)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.permute(_input_tensor, 0, 2, 1)
print('Output tensor: ', _output_tensor)