'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp_\ntorch.Tensor.ldexp_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
other = torch.randint(5, (3, 3), dtype=torch.int)
torch.Tensor.ldexp_(input_tensor, other)
print(input_tensor)