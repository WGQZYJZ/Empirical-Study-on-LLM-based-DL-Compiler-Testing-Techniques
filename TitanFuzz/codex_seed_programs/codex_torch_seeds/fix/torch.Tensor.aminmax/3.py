'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.aminmax(input_tensor, dim=None, keepdim=False)
print('Output tensor: ', output_tensor)