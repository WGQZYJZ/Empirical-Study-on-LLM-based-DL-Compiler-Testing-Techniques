'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input_data = torch.arange(0, 9, 1).view(3, 3)
print('Input data:')
print(input_data)
result_data = torch.flip(input_data, [1])
print('Result data:')
print(result_data)
print('Flip the first dim:')
result_data = torch.flip(input_data, [0])
print(result_data)