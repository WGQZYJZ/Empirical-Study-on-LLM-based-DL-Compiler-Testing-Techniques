'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_data = torch.Tensor(input_data)
print('input_data:', input_data)
output = torch.atleast_1d(input_data)
print('output:', output)