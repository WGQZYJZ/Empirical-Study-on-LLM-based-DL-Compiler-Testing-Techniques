'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
input_data = torch.rand(3, 3)
print('Input data: ', input_data)
input_data_type = torch.jit.annotate(input_data, input_data)
print('Input data type: ', input_data_type)