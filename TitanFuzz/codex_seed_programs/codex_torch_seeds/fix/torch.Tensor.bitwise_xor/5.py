'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
print('Input tensor: {}'.format(input_tensor))
output_tensor = input_tensor.bitwise_xor(input_tensor)
print('Output tensor: {}'.format(output_tensor))