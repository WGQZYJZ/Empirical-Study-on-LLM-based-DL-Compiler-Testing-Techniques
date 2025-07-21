'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
data = torch.rand(2, 3, 4)
print(data)
print(data.stride())
print(data.stride(0))
print(data.stride(1))
print(data.stride(2))
print(data.transpose(0, 1))
print(data.transpose(1, 2))
print(data.transpose(0, 2))