'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndim\ntorch.Tensor.ndim(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor.ndim())
print(input_tensor.size())
print(input_tensor.numel())
print(input_tensor.dim())
print(input_tensor.shape)
print(input_tensor.view(3, 8))
print(input_tensor.view(3, (- 1)))