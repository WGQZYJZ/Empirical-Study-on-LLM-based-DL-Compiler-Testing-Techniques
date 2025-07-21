'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
print(_input_tensor)
result = torch.Tensor.dot(_input_tensor, _input_tensor.T)
print(result)