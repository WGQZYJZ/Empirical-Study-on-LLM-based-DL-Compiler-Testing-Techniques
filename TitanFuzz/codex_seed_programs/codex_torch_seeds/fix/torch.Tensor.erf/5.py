'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erf\ntorch.Tensor.erf(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.erf(_input_tensor)
print('Input tensor:', _input_tensor)
print('Output tensor:', _output_tensor)