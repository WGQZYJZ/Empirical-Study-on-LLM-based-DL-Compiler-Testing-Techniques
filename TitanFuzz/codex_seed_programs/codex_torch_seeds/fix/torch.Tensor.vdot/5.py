'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vdot\ntorch.Tensor.vdot(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(3, 2)
print(torch.Tensor.vdot(input_tensor, other))