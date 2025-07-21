'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.amin(dim=1, keepdim=True)
print('Output tensor: ', output_tensor)