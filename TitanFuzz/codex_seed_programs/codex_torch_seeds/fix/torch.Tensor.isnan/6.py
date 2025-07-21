'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isnan\ntorch.Tensor.isnan(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, requires_grad=True)
_output_tensor = torch.Tensor.isnan(_input_tensor)
print('Output tensor: ', _output_tensor)