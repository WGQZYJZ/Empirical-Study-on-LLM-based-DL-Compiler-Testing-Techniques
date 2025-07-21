'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- float('inf')), (- 1), 0, 1, float('inf')])
output_tensor = torch.Tensor.isneginf(input_tensor)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)