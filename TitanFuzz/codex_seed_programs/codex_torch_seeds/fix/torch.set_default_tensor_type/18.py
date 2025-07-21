'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_data: ', input_data)
print('input_data.type: ', input_data.type())
torch.set_default_tensor_type(torch.DoubleTensor)
print('After call the API torch.set_default_tensor_type')
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_data: ', input_data)
print('input_data.type: ', input_data.type())