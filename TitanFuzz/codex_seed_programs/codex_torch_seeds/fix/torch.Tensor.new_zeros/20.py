'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
x = torch.randn(3, 4, 5)
y = torch.Tensor.new_zeros(x, size=(4, 5))
print(y)