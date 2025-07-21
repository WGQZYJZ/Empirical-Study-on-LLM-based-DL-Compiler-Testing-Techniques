'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input data:\n', input_data)
print('\nDim = 0, keepdim = False')
output_data = torch.all(input_data, dim=0, keepdim=False)
print('Output data:\n', output_data)
print('\nDim = 0, keepdim = True')
output_data = torch.all(input_data, dim=0, keepdim=True)
print('Output data:\n', output_data)
print('\nDim = 1, keepdim = False')
output_data = torch.all(input_data, dim=1, keepdim=False)
print('Output data:\n', output_data)