'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.arange((- 2), 3, 0.5)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', torch.Tensor.heaviside(input_tensor, (0, 1)))
print('Output Tensor: ', torch.Tensor.heaviside(input_tensor, (0.5, 1.5)))
print('Output Tensor: ', torch.Tensor.heaviside(input_tensor, (1, 2)))