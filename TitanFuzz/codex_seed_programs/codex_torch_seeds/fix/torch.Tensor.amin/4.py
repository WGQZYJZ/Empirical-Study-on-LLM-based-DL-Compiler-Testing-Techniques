'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(input_tensor))
output_tensor = torch.Tensor.amin(input_tensor, dim=1, keepdim=False)
print('Output tensor: {}'.format(output_tensor))