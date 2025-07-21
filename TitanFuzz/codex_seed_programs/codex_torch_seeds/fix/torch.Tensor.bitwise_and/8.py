'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (5, 5))
other = torch.randint(0, 2, (5, 5))
print('Input Tensor: \n', input_tensor)
print('Other: \n', other)
print('Bitwise AND: \n', torch.Tensor.bitwise_and(input_tensor, other))