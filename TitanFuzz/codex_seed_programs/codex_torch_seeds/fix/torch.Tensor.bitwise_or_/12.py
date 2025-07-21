'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_or_\ntorch.Tensor.bitwise_or_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.uint8)
print('Input tensor: \n{}'.format(input_tensor))
output_tensor = input_tensor.bitwise_or_(input_tensor)
print('Output tensor: \n{}'.format(output_tensor))