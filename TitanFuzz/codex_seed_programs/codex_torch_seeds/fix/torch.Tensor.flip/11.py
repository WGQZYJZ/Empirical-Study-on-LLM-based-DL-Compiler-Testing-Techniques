'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor:')
print(_input_tensor)
_flip_tensor = torch.Tensor.flip(_input_tensor, (1,))
print('Flip tensor:')
print(_flip_tensor)