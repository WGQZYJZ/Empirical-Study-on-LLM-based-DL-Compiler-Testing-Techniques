'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
output_data = torch.nn.functional.sigmoid(input_data)
print('Input data:\n', input_data)
print('Output data:\n', output_data)