'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10_\ntorch.Tensor.log10_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.log10_(_input_tensor)
print('Input tensor:\n', _input_tensor)
print('Output tensor:\n', output_tensor)