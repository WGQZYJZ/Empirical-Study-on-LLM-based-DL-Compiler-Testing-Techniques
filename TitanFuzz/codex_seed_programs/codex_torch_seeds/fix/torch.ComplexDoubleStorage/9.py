'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ComplexDoubleStorage\ntorch.ComplexDoubleStorage(*args, **kwargs)\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_data = torch.ComplexDoubleStorage(input_data)
print('input_data = ', input_data)
print('type(input_data) = ', type(input_data))