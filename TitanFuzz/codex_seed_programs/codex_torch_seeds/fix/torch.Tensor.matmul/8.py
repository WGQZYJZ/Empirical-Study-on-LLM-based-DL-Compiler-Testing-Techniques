'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(3, 2)
print(x)
print(y)
z = torch.matmul(x, y)
print(z)
z = x.matmul(y)
print(z)