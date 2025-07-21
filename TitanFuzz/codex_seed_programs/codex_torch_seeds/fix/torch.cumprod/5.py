'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input data: \n{}'.format(input_data))
output_data = torch.cumprod(input_data, dim=1)
print('Output data: \n{}'.format(output_data))