'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd\ntorch.Tensor.gcd(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=100, size=(5, 5))
other = torch.randint(low=0, high=100, size=(5, 5))
print('Input tensor:\n', input_tensor)
print('Other tensor:\n', other)
gcd_tensor = input_tensor.gcd(other)
print('GCD tensor:\n', gcd_tensor)