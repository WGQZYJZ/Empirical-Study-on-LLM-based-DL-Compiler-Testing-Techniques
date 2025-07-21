'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor:', _input_tensor)
torch.Tensor.apply_(_input_tensor, (lambda x: (x + 1)))
print('Output Tensor:', _input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable, args)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor:', _input_tensor)
torch.Tensor.apply_(_input_tensor, (lambda x, y: (x + y)), args=2)
print('Output Tensor:', _input_tensor)