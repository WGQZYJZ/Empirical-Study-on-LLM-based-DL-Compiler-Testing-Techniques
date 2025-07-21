'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.randn(4, 4)
torch.Tensor.addcdiv_(x, y, z, value=1)
print(x)
print(y)
print(z)