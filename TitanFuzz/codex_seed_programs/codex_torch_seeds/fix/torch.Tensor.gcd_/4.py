'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
_input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.int)
print('Input tensor: {}'.format(_input_tensor))
_gcd_value = torch.Tensor.gcd_(_input_tensor, other=torch.tensor(5))
print('GCD value: {}'.format(_gcd_value))