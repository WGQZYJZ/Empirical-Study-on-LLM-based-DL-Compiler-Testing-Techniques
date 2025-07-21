'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
print(input_tensor.ldexp(other))