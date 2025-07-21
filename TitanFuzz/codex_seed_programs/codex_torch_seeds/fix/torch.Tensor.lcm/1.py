'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lcm\ntorch.Tensor.lcm(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(10, (2, 3), dtype=torch.int)
print('Input tensor: {}'.format(input_tensor))
output = input_tensor.lcm(2)
print('Output tensor: {}'.format(output))