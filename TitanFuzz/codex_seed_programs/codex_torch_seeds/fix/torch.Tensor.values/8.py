'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 224, 224)
_output_tensor = torch.Tensor.values(_input_tensor)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)