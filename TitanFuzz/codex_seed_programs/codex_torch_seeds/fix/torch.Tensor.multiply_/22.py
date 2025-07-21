'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
x = torch.rand(5, 3)
y = torch.Tensor.multiply_(x, 10)
print(x)
print(y)