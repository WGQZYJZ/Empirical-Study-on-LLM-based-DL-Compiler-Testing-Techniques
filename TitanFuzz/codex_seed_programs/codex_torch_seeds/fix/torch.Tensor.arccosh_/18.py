'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh_\ntorch.Tensor.arccosh_(_input_tensor, )\n'
import torch
input_tensor = torch.tensor([(- 1.0), 0, 1.0, 2.0, 3.0])
output_tensor = torch.Tensor.arccosh_(input_tensor)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)