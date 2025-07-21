'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
input_data = torch.rand(4, 4)
print('Input data: ', input_data)
torch.set_default_tensor_type(torch.DoubleTensor)
print('Default tensor type: ', torch.get_default_dtype())
print('Default tensor type: ', torch.get_default_dtype())
print('Input data: ', input_data)
print('Type of input data: ', input_data.type())