'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor:')
print(_input_tensor)
print('torch.Tensor.isinf(_input_tensor):')
print(torch.Tensor.isinf(_input_tensor))