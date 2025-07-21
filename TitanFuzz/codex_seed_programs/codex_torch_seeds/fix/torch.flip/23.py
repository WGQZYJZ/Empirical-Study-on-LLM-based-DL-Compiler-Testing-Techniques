'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data: \n', input_data)
output_data = torch.flip(input_data, [0, 1])
print('Output data: \n', output_data)