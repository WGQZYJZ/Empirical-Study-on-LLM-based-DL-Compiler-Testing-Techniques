'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not\ntorch.Tensor.logical_not(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([[0, 0, 0], [1, 1, 1], [1, 0, 1]])
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.logical_not(input_tensor)
print('Output tensor: ', output_tensor)