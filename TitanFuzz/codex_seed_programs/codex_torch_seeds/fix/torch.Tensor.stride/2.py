'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
input_tensor = torch.rand(2, 3, 5, 5)
print('input_tensor.stride(1) = ', input_tensor.stride(1))
print('input_tensor.stride(2) = ', input_tensor.stride(2))
print('input_tensor.stride(3) = ', input_tensor.stride(3))