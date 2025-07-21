'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
input_data_1 = torch.randn(2, 3)
input_data_2 = torch.randn(2, 3)
print('input_data_1: ', input_data_1)
print('input_data_2: ', input_data_2)
output = torch.hstack((input_data_1, input_data_2))
print('output: ', output)