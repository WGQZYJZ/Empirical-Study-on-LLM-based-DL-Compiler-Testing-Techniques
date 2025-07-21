'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd\ntorch.Tensor.gcd(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(10, (3, 3))
print(input_tensor)
print(torch.Tensor.gcd(input_tensor, 3))