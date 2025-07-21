'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: {}'.format(input_tensor))
output_tensor = torch.flip(input_tensor, dims=[0, 1])
print('Output tensor: {}'.format(output_tensor))
print('Expected output tensor: {}'.format(input_tensor.flip(dims=[0, 1])))