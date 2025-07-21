'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input data: ', _input_tensor)
_output_tensor = torch.Tensor.trunc(_input_tensor)
print('Output data: ', _output_tensor)