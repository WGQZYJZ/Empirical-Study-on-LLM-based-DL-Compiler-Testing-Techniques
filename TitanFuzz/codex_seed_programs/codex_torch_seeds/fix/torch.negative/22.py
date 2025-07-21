'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input data:\n', input_data)
output_data = torch.negative(input_data)
print('Output data:\n', output_data)