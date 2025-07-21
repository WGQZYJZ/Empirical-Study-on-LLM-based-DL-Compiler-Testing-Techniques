'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.BoolStorage\ntorch.BoolStorage(*args, **kwargs)\n'
import torch
input_data = [True, False, True, False]
output_data = torch.BoolStorage(input_data)
print('\ninput_data: ', input_data)
print('\noutput_data: ', output_data)