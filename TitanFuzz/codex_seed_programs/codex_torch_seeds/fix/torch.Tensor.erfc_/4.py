'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfc_\ntorch.Tensor.erfc_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.erfc_(input_tensor)
print('Output tensor: ', output_tensor)