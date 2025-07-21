'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril\ntorch.Tensor.tril(_input_tensor, diagonal=0)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.tril(_input_tensor, diagonal=0)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)