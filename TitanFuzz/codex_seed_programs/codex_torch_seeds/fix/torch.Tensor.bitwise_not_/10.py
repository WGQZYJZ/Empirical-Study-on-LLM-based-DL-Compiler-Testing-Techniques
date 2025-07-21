'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)
print('Output tensor: \n', output_tensor)