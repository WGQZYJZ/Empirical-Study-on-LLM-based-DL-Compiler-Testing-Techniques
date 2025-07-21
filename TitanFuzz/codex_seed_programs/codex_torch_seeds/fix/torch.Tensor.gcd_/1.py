'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(1, 10, (5, 5), dtype=torch.int)
other = torch.randint(1, 10, (5, 5), dtype=torch.int)
print('Input tensor:', input_tensor)
print('Other:', other)
input_tensor.gcd_(other)
print('Result:', input_tensor)