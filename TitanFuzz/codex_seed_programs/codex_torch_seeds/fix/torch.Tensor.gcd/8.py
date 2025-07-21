'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd\ntorch.Tensor.gcd(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
other = torch.randn(2, 3, 5)
gcd_output = input_tensor.gcd(other)
print(gcd_output)