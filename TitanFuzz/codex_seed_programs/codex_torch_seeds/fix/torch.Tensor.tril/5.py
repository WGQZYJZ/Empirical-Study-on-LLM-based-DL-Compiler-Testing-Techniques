'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril\ntorch.Tensor.tril(_input_tensor, diagonal=0)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(3, 3))
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_input_tensor.tril())
print('Output tensor (diagonal=1):')
print(_input_tensor.tril(diagonal=1))