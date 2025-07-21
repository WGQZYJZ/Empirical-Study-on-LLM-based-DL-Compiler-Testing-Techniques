'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagflat\ntorch.Tensor.diagflat(_input_tensor, offset=0)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3))
print('Input tensor: {}'.format(input_tensor))
output_tensor = torch.Tensor.diagflat(input_tensor, offset=0)
print('Output tensor: {}'.format(output_tensor))
output_tensor = torch.diagflat(input_tensor, offset=0)
print('Output tensor: {}'.format(output_tensor))