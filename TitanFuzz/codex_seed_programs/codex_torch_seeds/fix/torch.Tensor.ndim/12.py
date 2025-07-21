'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndim\ntorch.Tensor.ndim(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print(_input_tensor.ndim())
print(_input_tensor.shape)
print(_input_tensor.size())
print(_input_tensor.numel())
print(_input_tensor.nelement())
print(_input_tensor.dim())
print(_input_tensor.reshape(3, 2))
_input_tensor_1 = torch.rand(2, 3)