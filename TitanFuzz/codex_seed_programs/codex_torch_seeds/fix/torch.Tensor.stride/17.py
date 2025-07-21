'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print(_input_tensor.stride())
print(_input_tensor.stride(0))
print(_input_tensor.stride(1))
print(_input_tensor.stride(2))
print(_input_tensor.stride(3))