'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, dtype=torch.float)
output_tensor = torch.Tensor.round(input_tensor)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)