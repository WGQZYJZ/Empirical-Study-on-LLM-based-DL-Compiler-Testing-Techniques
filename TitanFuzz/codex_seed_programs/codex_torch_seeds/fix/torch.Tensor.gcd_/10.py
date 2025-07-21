'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(10, dtype=torch.float64)
other = torch.randn(10, dtype=torch.float64)
torch.Tensor.gcd_(input_tensor, other)
print(input_tensor)