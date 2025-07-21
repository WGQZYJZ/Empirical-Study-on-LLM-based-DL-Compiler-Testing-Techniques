'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
a = torch.randint(1, 10, (3, 4))
b = torch.randint(1, 10, (3, 4))
torch.gcd(a, b)
a.gcd_(b)
print(a)