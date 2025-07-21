'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
input_data = torch.rand(1, 1, 3, 3)
print('Input data is: ', input_data)
print('Input data type is: ', input_data.type())
real_data = torch.real(input_data)
print('Real data is: ', real_data)
print('Real data type is: ', real_data.type())