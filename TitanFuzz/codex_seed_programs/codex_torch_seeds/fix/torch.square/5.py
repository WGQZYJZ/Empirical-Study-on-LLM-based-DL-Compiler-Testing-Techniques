'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
output_data = torch.square(input_data)
print('The input is {}'.format(input_data))
print('The output is {}'.format(output_data))