'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(3, 4)
torch.Tensor.remainder_(a, b)
print(a)