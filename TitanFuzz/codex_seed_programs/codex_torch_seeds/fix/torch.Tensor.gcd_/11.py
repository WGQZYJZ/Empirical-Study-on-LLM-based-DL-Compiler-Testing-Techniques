'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=1, high=100, size=(3, 3), dtype=torch.int32)
print('Input tensor: ', input_tensor)
gcd_value = input_tensor.gcd_(input_tensor)
print('Greatest common divisor: ', gcd_value)