'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:\n', _input_tensor)
_output_tensor = torch.Tensor.neg(_input_tensor)
print('Output tensor:\n', _output_tensor)