'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print(input_tensor.stride())
print(input_tensor.stride(0))
print(input_tensor.stride(1))
print(input_tensor.stride(2))
print(input_tensor.stride(3))