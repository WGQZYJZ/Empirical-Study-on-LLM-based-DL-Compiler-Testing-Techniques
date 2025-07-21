'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data: ', input_data)
torch.set_default_dtype(torch.float64)
print('Default data type: ', torch.get_default_dtype())
print('Input data type: ', input_data.dtype)