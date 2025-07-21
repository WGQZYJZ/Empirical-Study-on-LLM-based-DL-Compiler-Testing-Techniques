'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
import torch
input_tensor = torch.randn(3, 3, 3)
print(input_tensor.stride(dim=0))
print(input_tensor.stride(dim=1))
print(input_tensor.stride(dim=2))
print(input_tensor.stride())