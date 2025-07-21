'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
_input_tensor = torch.randn(10, 10)
_output_tensor = torch.Tensor.heaviside(_input_tensor, values=None)
print('Input data: ', _input_tensor)
print('Output data: ', _output_tensor)