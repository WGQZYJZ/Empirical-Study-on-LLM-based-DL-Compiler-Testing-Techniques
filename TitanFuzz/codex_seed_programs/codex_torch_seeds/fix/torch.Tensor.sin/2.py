'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sin\ntorch.Tensor.sin(_input_tensor)\n'
import torch
_input_tensor = torch.rand(1, 3, 3)
print('Input Tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.sin(_input_tensor)
print('Output Tensor:')
print(_output_tensor)