'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data:\n', input_data)
norm_input_data = torch.linalg.norm(input_data)
print('Norm of input data: ', norm_input_data)
norm_input_data_along_0 = torch.linalg.norm(input_data, dim=0)
print('Norm of input data along the dimension 0: ', norm_input_data_along_0)
norm_input_data_along_1 = torch.linalg.norm(input_data, dim=1)
print('Norm of input data along the dimension 1: ', norm_input_data_along_1)