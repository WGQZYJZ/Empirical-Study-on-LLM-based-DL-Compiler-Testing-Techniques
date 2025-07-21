'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
input_data = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input data is: \n {}'.format(input_data))
print('Shape of input data is: {}'.format(input_data.shape))
flipped_input_data = torch.flipud(input_data)
print('Flipped input data is: \n {}'.format(flipped_input_data))
print('Shape of flipped input data is: {}'.format(flipped_input_data.shape))