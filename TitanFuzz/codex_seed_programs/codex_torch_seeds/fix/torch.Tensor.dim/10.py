'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dim\ntorch.Tensor.dim(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor.dim())
print(input_tensor.size())
print(input_tensor.shape)
print(input_tensor.numel())
print(input_tensor.nelement())