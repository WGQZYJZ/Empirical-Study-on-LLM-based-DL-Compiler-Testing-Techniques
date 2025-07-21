'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
count_nonzero = torch.count_nonzero(input_data)
print('Count non-zero: ', count_nonzero)
count_nonzero = torch.count_nonzero(input_data, dim=0)
print('Count non-zero along the dimension 0: ', count_nonzero)
count_nonzero = torch.count_nonzero(input_data, dim=1)
print('Count non-zero along the dimension 1: ', count_nonzero)