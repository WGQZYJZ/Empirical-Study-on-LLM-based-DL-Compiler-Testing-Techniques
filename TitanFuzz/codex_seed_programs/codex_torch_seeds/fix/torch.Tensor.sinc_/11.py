'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinc_\ntorch.Tensor.sinc_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 10)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.sinc_(_input_tensor)
print('Output tensor: ', _output_tensor)