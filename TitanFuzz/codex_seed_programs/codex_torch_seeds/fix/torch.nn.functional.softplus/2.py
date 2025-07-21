'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(5)
print('Input data: ', input_data)
print('Task 3: Call the API torch.nn.functional.softplus')
output_data = torch.nn.functional.softplus(input_data)
print('Output data: ', output_data)