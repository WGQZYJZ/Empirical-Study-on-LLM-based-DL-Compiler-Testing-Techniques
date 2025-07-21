'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor: ', input_tensor)
output_tensor = torch.atleast_1d(input_tensor)
print('Output tensor: ', output_tensor)