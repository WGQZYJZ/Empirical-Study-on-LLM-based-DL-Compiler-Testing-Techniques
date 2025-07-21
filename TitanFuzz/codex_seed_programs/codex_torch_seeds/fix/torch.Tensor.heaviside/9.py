'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
_input_tensor = torch.randn(5, 5)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.heaviside(_input_tensor, 0)
print('Output tensor: ', _output_tensor)