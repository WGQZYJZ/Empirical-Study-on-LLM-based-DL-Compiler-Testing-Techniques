'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder\ntorch.Tensor.remainder(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randn(2, 3)
divisor = 2
print('input_tensor = {}'.format(input_tensor))
print('divisor = {}'.format(divisor))
remainder = input_tensor.remainder(divisor)
print('remainder = {}'.format(remainder))