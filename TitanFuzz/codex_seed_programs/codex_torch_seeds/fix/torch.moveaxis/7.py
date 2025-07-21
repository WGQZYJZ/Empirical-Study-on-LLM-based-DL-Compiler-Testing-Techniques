'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input_data = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
output_data = torch.moveaxis(input_data, 0, 1)
print('input_data = \n', input_data)
print('output_data = \n', output_data)