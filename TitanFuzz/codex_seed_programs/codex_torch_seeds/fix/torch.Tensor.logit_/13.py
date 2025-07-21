'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit_\ntorch.Tensor.logit_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, requires_grad=True)
output_tensor = torch.Tensor.logit_(input_tensor)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)