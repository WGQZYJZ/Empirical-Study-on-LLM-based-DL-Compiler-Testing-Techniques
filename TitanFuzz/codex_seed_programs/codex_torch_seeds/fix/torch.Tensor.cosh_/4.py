'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh_\ntorch.Tensor.cosh_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1), 0, 1])
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.cosh_(input_tensor)
print('Output tensor: ', output_tensor)