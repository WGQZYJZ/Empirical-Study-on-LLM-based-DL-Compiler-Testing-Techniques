'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('Input data:')
print(input_data)
output_data = torch.reshape(input_data, (4, 2))
print('Output data:')
print(output_data)