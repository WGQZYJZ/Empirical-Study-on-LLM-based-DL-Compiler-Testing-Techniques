'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
input_data = torch.randn(1, 1, 2, 2)
torch.get_default_dtype()
print('The data type of input_data is: ', input_data.dtype)
print('The data type of torch.get_default_dtype is: ', torch.get_default_dtype())
input_data = input_data.type(torch.float64)
print('The data type of input_data is: ', input_data.dtype)