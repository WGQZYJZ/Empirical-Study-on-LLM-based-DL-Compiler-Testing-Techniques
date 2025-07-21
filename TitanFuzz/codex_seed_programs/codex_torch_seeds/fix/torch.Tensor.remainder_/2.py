'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(1,), dtype=torch.float)
print('Generated input: ', input_tensor)
remainder = torch.Tensor.remainder_(input_tensor, 2)
print('Remainder: ', remainder)